Status: published
Date: 2021-09-09 15:21:21
Modified: 2021-10-19 23:40:16
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
    <td> GitHub SSH Key </td>
    <td> A SSH public key </td>
    <td> All repos </td>
    <td> Read and Write </td>
    <th> SSH </th>
  </tr>

  <tr>
    <td> GitHub Deploy Key </td>
    <td> A SSH public key </td>
    <td> Single repo </td>
    <td> Read (optionally write) </td>
    <th> SSH </th>
  </tr>

  <tr>
    <td> GitHub Personal Access Token </td>
    <td> </td>
    <td> All public repos (optionally private repos) </td>
    <td> Read and Write </td>
    <th> HTTPS </th>
  </tr>

  <tr>
    <td> GitHub Repository Secret </td>
    <td> Repo secret for <br> authenticating <br> GitHub actions, etc.</td>
    <td> Single repo </td>
    <td> Read and Write </td>
    <th> HTTPS </th>
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
