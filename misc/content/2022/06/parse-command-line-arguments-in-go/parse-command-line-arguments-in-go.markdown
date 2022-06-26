Status: published
Date: 2022-06-10 20:18:20
Modified: 2022-06-13 14:39:44
Author: Benjamin Du
Slug: parse-command-line-arguments-in-go
Title: Parse Command Line Arguments in Go
Category: Computer Science
Tags: Computer Science, programming, Go, GoLANG, parse, command, line, argument, flag, viper

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. [flag](https://pkg.go.dev/flag)
    is a Go standard library for parsing command-line arguments.
    It is simple but limited.
    For more discussions,
    please refer to
    [Parse Command Line Arguments Using Flag in Go](https://www.legendu.net/misc/blog/parse-command-line-arguments-using-flag-in-go/)
    .

2. [spf13/cobra](https://github.com/spf13/cobra),
    [urfave/cli](https://github.com/urfave/cli),
    and
    [spf13/viper](https://github.com/spf13/viper)
    are popular good 3rd-party libraries.
    [spf13/cobra](https://github.com/spf13/cobra)
    is the most popular one 
    and is used in many Go projects such as Kubernetes, Hugo, Github CLI, etc. 
    [spf13/viper](https://github.com/spf13/viper)'s power is on application configuration 
    even though it can also be used to parse command-line arguments.

To sum up,
I'd suggest using 
[spf13/cobra](https://github.com/spf13/cobra) 
for parsing command-line arguments 
and
[spf13/viper](https://github.com/spf13/viper)
for application configuration.

## References

- [Parse Command Line Arguments Using Flag in Go](https://www.legendu.net/misc/blog/parse-command-line-arguments-using-flag-in-go/)

- [Sting of the Viper: Getting Cobra and Viper to work together](https://carolynvanslyck.com/blog/2020/08/sting-of-the-viper/)

