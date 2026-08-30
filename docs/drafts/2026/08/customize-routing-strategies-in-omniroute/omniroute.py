# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "requests>=2.34.2",
# ]
# ///
"""Thin client for the OmniRoute combos REST API."""

from collections.abc import Iterable
from typing import Any

import requests

DEFAULT_TIMEOUT = 30


class OmniRoute:
    """Thin client for the OmniRoute combos REST API."""

    def __init__(self, token: str, base_url: str = "http://localhost:20128") -> None:
        """Create a client bound to one OmniRoute instance.

        :param token: Bearer token sent in the ``Authorization`` header of every request.
        :param base_url: Root URL of the OmniRoute instance; trailing slashes are stripped.
        """
        self.token = token
        self.base_url = base_url.rstrip("/")

    def _request(
        self,
        method: str,
        path: str,
        *,
        raise_for_status: bool = True,
        **kwargs: Any,
    ) -> Any:
        """Send an authenticated request and return the decoded JSON body.

        :param method: HTTP method, e.g. ``"GET"`` or ``"POST"``.
        :param path: Path appended to ``base_url``, e.g. ``"/api/combos"``.
        :param raise_for_status: When ``True``, raise for a 4xx/5xx response.
        :param kwargs: Extra keyword arguments forwarded to ``requests.request``
            (for example ``json=...``); ``timeout`` defaults to ``DEFAULT_TIMEOUT``.
        :return: The response body parsed as JSON, or ``None`` for an empty body.
        """
        kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
        resp = requests.request(
            method,
            f"{self.base_url}{path}",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}",
            },
            **kwargs,
        )
        if raise_for_status:
            resp.raise_for_status()
        return resp.json() if resp.content else None

    def list_combos(self, raise_for_status: bool = True) -> list[dict[str, Any]]:
        """Return every combo currently defined on the instance.

        :param raise_for_status: When ``True``, raise for a 4xx/5xx response.
        :return: A list of combo objects.
        """
        data = self._request("GET", "/api/combos",
                             raise_for_status=raise_for_status)
        return data["combos"]

    def combos_by_name(self) -> dict[str, dict[str, Any]]:
        """Return the existing combos keyed by name, using a single API call.

        :return: A mapping of combo ``name`` to the combo object.
        """
        return {combo["name"]: combo for combo in self.list_combos()}

    def get_combo(self, name: str) -> dict[str, Any] | None:
        """Look up a single existing combo by name.

        :param name: The combo name to look for.
        :return: The matching combo object, or ``None`` if no combo has that name.
        """
        return self.combos_by_name().get(name)

    def delete_combo(
        self, combo_id: str, raise_for_status: bool = True
    ) -> dict[str, Any] | None:
        """Delete the combo with the given id.

        :param combo_id: The ``id`` of the combo to delete (not its name).
        :param raise_for_status: When ``True``, raise for a 4xx/5xx response.
        :return: The response body parsed as JSON, or ``None`` for an empty body.
        """
        return self._request(
            "DELETE", f"/api/combos/{combo_id}", raise_for_status=raise_for_status
        )

    def add_combo(
        self,
        combo: dict[str, Any],
        replace: bool = True,
        existing: dict[str, dict[str, Any]] | None = None,
        raise_for_status: bool = True,
    ) -> dict[str, Any]:
        """Create a combo, optionally deleting any existing combo of the same name first.

        :param combo: The combo definition to POST; must contain a ``name``.
        :param replace: When ``True``, delete a pre-existing combo with the same
            ``name`` before creating this one (OmniRoute rejects a duplicate name).
        :param existing: Pre-fetched ``name -> combo`` map to consult instead of
            calling the API again; ignored when ``replace`` is ``False``. When
            ``None`` and ``replace`` is ``True``, it is fetched via
            :meth:`combos_by_name`.
        :param raise_for_status: When ``True``, raise for a 4xx/5xx response on
            the create request.
        :return: The created combo object.
        """
        if replace:
            if existing is None:
                existing = self.combos_by_name()
            old = existing.get(combo["name"])
            if old is not None:
                self.delete_combo(old["id"])
        return self._request(
            "POST", "/api/combos", raise_for_status=raise_for_status, json=combo
        )

    def add_combos(
        self,
        combos: Iterable[dict[str, Any]],
        replace: bool = True,
        raise_for_status: bool = True,
    ) -> list[dict[str, Any]]:
        """Create several combos in order, reusing one existing-combos lookup.

        :param combos: An iterable of combo definitions, each with a ``name`` that
            is unique within the iterable. Processed in order, so a nested child
            combo should come before the parent that references it.
        :param replace: When ``True``, delete a pre-existing combo with the same
            ``name`` before creating each one.
        :param raise_for_status: When ``True``, raise for a 4xx/5xx response on
            any create request.
        :return: The created combo objects, in input order.
        """
        # Fetch the existing combos once and reuse it for every add.
        existing = self.combos_by_name() if replace else None
        return [
            self.add_combo(
                combo,
                replace=replace,
                existing=existing,
                raise_for_status=raise_for_status,
            )
            for combo in combos
        ]
