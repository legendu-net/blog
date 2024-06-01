Status: published
Date: 2024-05-17 01:53:15
Modified: 2024-05-22 23:22:23
Author: Benjamin Du
Slug: tips-on-microsoft-graph-apis
Title: Tips on Microsoft Graph APIs
Category: Computer Science
Tags: Computer Science, programming, API, Microsoft, Graph, mail, email, Outlook

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://developer.microsoft.com/graph/graph-explorer


https://learn.microsoft.com/en-us/graph/use-the-api

## List Mail Folders

https://graph.microsoft.com/beta/me/mailFolders?%24skip=40

```
from msgraph import GraphServiceClient
from msgraph.generated.users.item.mailFolders.mail_folders_request_builder import MailFoldersRequestBuilder

graph_client = GraphServiceClient(credentials, scopes)

query_params = MailFoldersRequestBuilder.MailFoldersRequestBuilderGetQueryParameters(
		skip = 40,
)

request_configuration = MailFoldersRequestBuilder.MailFoldersRequestBuilderGetRequestConfiguration(
query_parameters = query_params,
)

result = await graph_client.me.mail_folders.get(request_configuration = request_configuration)
```

## List Messages In One of My Folders

https://graph.microsoft.com/beta/me/mailFolders/AQMkADAwATM3ZmYAZS1kODllLWVlAGFmLTAwAi0wMAoALgAAA5IYc1lGcqZFqycmUUviCS0BAGPETpcnddlKjf81XGKfopwAAXCPckgAAAA=/messages

```
from msgraph import GraphServiceClient

graph_client = GraphServiceClient(credentials, scopes)


result = await graph_client.me.mail_folders.by_mail_folder_id('mailFolder-id').messages.get()
```

## References

- [Connecting to Microsoft Graph API with Python msal library.](https://www.youtube.com/watch?v=wAIZn6RDSJg)
