# What?

A dummy Python project that illustrates a potential bug in https://github.com/jbms/sphinx-immaterial.

# Reproduce

```console
pip install -R requirements.txt
cd ./docs
make html
```

This will result in the following error:

```
Extension error (sphinx_immaterial.apidoc.python.apigen):
Handler <function _builder_inited at 0x7ff079d9d8a0> for event 'builder-inited' threw an exception (exception: Cannot set values to nptyping.NDArray.)
make: *** [Makefile:20: html] Error 2
```

If we exclude `dummy/typing.py` module by commenting it out in `docs/source/conf.py`:

```python
# Python apigen configuration
python_apigen_modules = {
    "dummy": "api/dummy.",
    # "dummy.typing": "api/dummy.typing.",
}
```

and try again:

```console
make html
```

the error goes away.

# Note

I'm not sure if the error is caused by `sphinx-immaterial`, `sphinx`, or `nptyping` package.
