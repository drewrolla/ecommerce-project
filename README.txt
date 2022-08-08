Git Cloned Shoha's repo.
Errors I came across:
AttributeError
FlushError - this was because i forgot to assign an id with a primary key to a table
BuildError - caused by an incorrectly named variable(?), something was mislabeled and it caused it
StaleError - this is still a bug in my code, so if you add more than one of the same item but try to remove just one, it throws that. Still working that one out
