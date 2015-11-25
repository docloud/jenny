# Jenny

**Note**: It's in alpha, don't use it on your production.

# Install

    make develop

# Usage


```python
from jenny import compile

compile("# Jenny\n\n Jenny Demo", "markdown", "html")

>>> '<h1 id="jenny">Jenny</h1>\n<p>Jenny Demo</p>\n'
```

## Timeline

- Wrapper for pandoc
- Implement with EBNF form
