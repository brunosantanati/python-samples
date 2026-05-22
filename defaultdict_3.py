from collections import defaultdict

"""
Unique Collections (defaultdict(set))
If you want to group items but ensure there are no duplicates, you can use set. Calling set() gives you a fresh, empty set set().
"""

# Tracking which unique tags a blog post has
blog_tags = defaultdict(set)

blog_tags["Post A"].add("Python")
blog_tags["Post A"].add("Coding")
blog_tags["Post A"].add("Python")  # Duplicate! Set handles it.

print(dict(blog_tags))
# Output: {'Post A': {'Coding', 'Python'}}

print(blog_tags)