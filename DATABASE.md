## Database format

Main Sqlite database is contained inside `database/database.db`.

> [!WARNING]
> Database will not contains JSON in the future

> This database is used to index JSON object by keys. Each field contains a `document` field which is a JSON containing complete object.

The database contains the following tables:

- **users**; fields `id`, `username`, `document` (doc: User)
- **courses**; fields `id`, `prof`, `start`, `end`, `document` (doc: Course)
- **classes**; fields `id`, `document` (doc: Class)
- **homeworks**; fields `id`, `prof`, `date` (doc: Homework)
- **timelines**; fields `id`, `classe`, `type`, `document` (doc: Event | Postit)
- **grades**; fields `id`, `student`, `document` (doc: Grade)
- **communicationBook**; fields `id`, `student`, `document` (doc: Coress)

## Special databases

- `data/cloud.db`; contains information about cloud
- `data/workspaces.db`; contains workspaces
- `data/`

## References

> [!TIP]
> References are not all written yet ! Help us by improving this documentation
