Status: published
Date: 2021-09-09 15:21:21
Modified: 2021-10-25 18:51:22
Author: Benjamin Du
Slug: comparison-of-github-tokens-and-keys
Title: Comparison of GitHub Tokens and Keys
Category: Computer Science
Tags: Computer Science, programming, GitHub, Git, security, token, key, SSH, public, private

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

<table style="width:100%">
  <tr>
    <th> Name </th>
    <th> Short Description </th>
    <th> Scope </th>
    <th> Permission </th>
    <th> Protocol </th>
  </tr>

  <tr>
    <td> GitHub <br> SSH Key </td>
    <td> A SSH public key </td>
    <td> All repos </td>
    <td> Read and Write </td>
    <th> SSH </th>
  </tr>

  <tr>
    <td> GitHub <br> Deploy Key </td>
    <td> A SSH public key </td>
    <td> Any repo <br> configures <br> the key </td>
    <td> Read (optionally write) </td>
    <th> SSH </th>
  </tr>

  <tr>
    <td> GitHub PAT </td>
    <td> Personal access token </td>
    <td> Any repo <br> configures <br> the PAT </td>
    <td> Read and Write </td>
    <th> HTTPS </th>
  </tr>

  <tr>
    <td> Repository Secret </td>
    <td> Repo secret (SSH keys, PATs or anything) for <br> authenticating GitHub APIs </td>
    <td> Single repo </td>
    <td> Depends </td>
    <th> Depends </th>
  </tr>

  <tr>
    <td> Organization Secret </td>
    <td> Org secret (SSH keys, PATs, or anything) for authenticating GitHub APIs </td>
    <td> All repos <br> in the org </td>
    <td> Depends </td>
    <th> Depends </th>
  </tr>

</table>

## Personal Access Tokens

[How to create a Github read-only API token](https://pmihaylov.com/github-readonly-api-token/)

## Deploy Keys

Deploy Keys are SSH keys which access restricted to a specific repository only.

https://developer.github.com/v3/guides/managing-deploy-keys/#deploy-keys

https://docs.github.com/en/developers/overview/managing-deploy-keys#deploy-keys

## References

- [Creating a personal access token for the command line](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
