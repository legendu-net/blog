Status: published
Date: 2022-11-12 14:31:12
Modified: 2023-05-10 17:01:16
Author: Benjamin Du
Slug: tips-on-protobuf
Title: Tips on Protobuf
Category: Computer Science
Tags: Computer Science, programming, protobuf, protocol buffer

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## oneof vs enum

Prefer to have oneof with a string field describing the specific type of oneof.

    message A { // A here is the "interface".
      string name = 1;
      string a_type = 2; // Or an enum. See AIP-126 and AIP-143 for more information.

      // .. Anything else that applies to all A's.

      // Stuff that's specific to the concrete types.
      oneof content {
        B b = 3;
        C c = 4;
        // ...
      }
    }

## References

- [Protocol Buffers Crash Course](https://www.youtube.com/watch?v=46O73On0gyI&t=6s)

- [Protobuf all the way down · Ainsley Escorce-Jones](https://www.youtube.com/watch?v=4784u5PRc5o&list=PLXY4_qxp8fUfML_FrAJN-OPfvg2DiqtIk&index=7)

- [AIP 126](https://google.aip.dev/126)

- [AIP 143](https://google.aip.dev/143)

- [Protobuf Overview](https://developers.google.com/protocol-buffers/docs/overview)

- [Protobuf @ GitHub](https://github.com/protocolbuffers/protobuf) 

- [Protocol Buffers](https://developers.google.com/protocol-buffers/)
