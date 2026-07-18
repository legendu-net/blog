---
title: Comparison of GitHub Tokens and Keys
created: '2021-09-09T15:21:21-07:00'
date: '2026-07-18T01:31:04-07:00'
authors:
  - bendu
label: comparison-of-github-tokens-and-keys
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - GitHub
  - Git
  - security
  - token
  - key
  - SSH
  - public
  - private
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Comparison of GitHub Tokens and Keys

```{list-table} Authentication Comparison
---
header-rows: 1
widths: 15 10 15 20 40
---
* - Credential Type
  - Protocol
  - Auth Boundary
  - Repository Granularity
  - Best For...
* - **GitHub SSH Key**
  - SSH
  - Bound to your **User Account**
  - All repositories you have access to
  - Day-to-day local development.
* - **Deploy Key**
  - SSH
  - Bound to a **Single Repository**
  - Exactly one repository
  - CI/CD pipelines, staging/production servers pulling a specific codebase.
* - **PAT (Classic)**
  - HTTPS
  - Bound to your **User Account**
  - Broad scopes (e.g., all private repos)
  - Legacy tools or quick API scripts that require broad account-level access.
* - **Fine-Grained PAT**
  - HTTPS
  - Bound to **Specific Owners/Repos**
  - Target single or selected repositories
  - Modern API access, secure automation, and third-party tools needing limited access.

```

## Repository and Organization-level Secrets

Any value,
e.g., keys/tokens (from GitHub and other services),
user/bot names, URLs, etc,
can be configured as secrets at repository or organization level
so that they can be used in workflows.
A repository-level secret is visible to the repository itself
while an organization-level secret is visible to all eligible repositories in the organization.

### Organization-level Secrets

GitHub Free organizations cannot share organization-level secrets with private repositories.
On the GitHub Free tier, organization-wide secrets are strictly restricted to public repositories.
If your workflows running inside private repositories attempt to call these organizational secrets,
they will return empty values and fail.
To resolve this limitation, choose one of the options below.

#### Option 1: Replicate Secrets at the Repository Level (Free)

The most common workaround on the free tier is to manually add the secret directly into the private repository's settings.

1. Navigate to your specific private repository on GitHub.Click Settings -> Secrets and variables -> Actions.
1. Click New repository secret.
1. Define the secret name and value, then click Add secret.

#### Option 2: Use Environment-Level Secrets (Free)

If you want to scope secrets specifically to deployment stages (like production or staging) without paying for an upgrade, use Environment secrets.

1. Inside your private repository, go to Settings -> Environments.
1. Create or select an environment.
1. Scroll to Environment secrets and add your variables.
1. Reference the environment in your workflow YAML file using the environment: key.

#### Option 3: Upgrade to GitHub Team or Enterprise (Paid)

If managing duplicate repository secrets becomes a security risk or operational hassle, upgrading your organization account resolves this restriction globally.
Both the GitHub Team and GitHub Enterprise paid tiers unlock the ability to share organization-level secrets with private and internal repositories seamlessly.

```{tip}
Check out
{ref}`reduce-operational-burdens-managing-secrets-without-a-paid-github-plan`
.
```

### Secrets vs. Environment Secrets

```{list-table} GitHub Secrets vs. Environment Secrets
---
widths: 20 40 40
header-rows: 1
---
* - Feature
  - Repository/Org Secrets
  - Environment Secrets
* - **Scope**
  - Global across the entire repo or organization.
  - Tied strictly to a specific deployment stage.
* - **Organization Level**
  - Fully supported (can share across multiple repos).
  - Not supported (must be defined per repo).
* - **Plaintext Support**
  - No (only supports encrypted values).
  - Yes (via accompanying Environment Variables).
* - **Approval Gates**
  - No (runs automatically on trigger).
  - Yes (can require manual approval to unlock).
* - **Branch Restrictions**
  - No (any branch with action access can read).
  - Yes (can limit access to specific branches).
```

Environment secrets offer much better security boundaries (like branch protection and manual approvals),
but they trade away central management.
Because you have to configure them inside every single repository,
they create a noticeable operational bottleneck as your engineering team scales up.

```{tip}
Check out
{ref}`reduce-operational-burdens-managing-secrets-without-a-paid-github-plan`
.
```

(reduce-operational-burdens-managing-secrets-without-a-paid-github-plan)=

## Reduce Operational Burdens Managing Secrets Without a Paid GitHub Plan

### Automation via GitHub API/CLI

Instead of clicking through the web interface for dozens of repositories,
you can use the GitHub CLI (gh) to automate environment and secret creation.

### Centralized Reusable Workflows

You can isolate your sensitive logic in a single, central repository.
Other repositories call this central workflow and use secrets:
inherit to pass context down safely,
reducing the configuration footprint in downstream projects.

### External Secret Vaults

Many organizations use GitHub secrets solely to store a single OIDC trust token.
The workflow then authenticates against a central manager like HashiCorp Vault
or AWS Secrets Manager to pull the required stage keys dynamically during the run based on the repository name.

## Deploy Keys

Deploy Keys are SSH keys which access restricted to a specific repository only.

https://developer.github.com/v3/guides/managing-deploy-keys/#deploy-keys

https://docs.github.com/en/developers/overview/managing-deploy-keys#deploy-keys

## GITHUB_TOKEN

- [Limitation of GITHUB_TOKEN](https://share.gemini.google/QW2ytbpZESgN)

## References

- [Creating a personal access token for the command line](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

- [How to create a Github read-only API token](https://pmihaylov.com/github-readonly-api-token/)
