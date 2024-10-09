# SeeMee

SeeMee is a tool to schedule hangouts with friends!

Link to what front-end will kind of look like:
https://excalidraw.com/#json=by9MpSCg_vLY_iD-N5qGV,cPOlUHBYXkGMhHZUMJrwYQ

## How to run

To run locally without debugger on:

```bash
flask --app main run 
```
To run locally with debugger on to automatically reload if code changes and show debugger in browser:
```bash
flask --app main run --debug
```
To run publicly
```bash
flask --app main run  --host=0.0.0.0
```
## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
