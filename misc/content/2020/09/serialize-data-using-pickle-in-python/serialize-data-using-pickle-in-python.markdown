Status: published
Date: 2020-09-03 09:42:01
Author: Benjamin Du
Slug: serialization-and-deserialization-in-python
Title: Serialization and deserialization in Python
Category: Computer Science
Tags: Computer Science, pickle, serialization, deserialization, JSON, cloudpickle, dill
Modified: 2022-05-13 09:41:22

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

1. [json](https://docs.python.org/3/library/json.html)
    is a simple built-in serialization and deserialization tool in Python.
    It is suggested that you avoid using it.
    For reasons backing this suggestion,
    please refer to.
    If serialization and deserialization is done only in Python,
    [Pickle](http://www.legendu.net/misc/blog/serialize-and-deserialize-object-using-pickle-in-python)
    is a much better alternative.

2. [Pickle](http://www.legendu.net/misc/blog/serialize-and-deserialize-object-using-pickle-in-python)
    is the most popular serialization and deserialization tool in Python.
    It supports serializing/deserializing most (even not all) Python classes.

3. [Dill](https://github.com/uqfoundation/dill)
    extends Python's
    [Pickle](http://www.legendu.net/misc/blog/serialize-and-deserialize-object-using-pickle-in-python)
    module for serializing and de-serializing Python objects to the majority of the built-in python types. 
    It also provides some good diagnostic tools for pickling, 
    the best of which is the pickle trace.
    For more discussions,
    please refer to
    [How to check which detail of a complex object cannot be pickled](https://stackoverflow.com/questions/22233478/how-to-check-which-detail-of-a-complex-object-cannot-be-pickled)
    .

4. cloudpickle

5. Use Parquet for pandas DataFrame.

## References

[How to check which detail of a complex object cannot be pickled](https://stackoverflow.com/questions/22233478/how-to-check-which-detail-of-a-complex-object-cannot-be-pickled)
