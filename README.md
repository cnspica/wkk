# WKK - wdxtub's Knowledge Kit

`WKK` is a set of tools that help me to get specific information I need, arrange my notes in a natural way as well as analyze the content of my notes and give me recommendations about books, wikis & news.

It can be regarded as an application that combines Evernote, RSS, Wikipedia together to make information retrieval/management easier.

`WKK` has the following modules:

+ `jarvis`: Personal Information Assistant(PIA), the brain of the `WKK` system
+ `nomadic`: A lightweight notes management system
+ `util`: Useful tools to import/export notes and other management actions

---

### Outlines of this README

<!-- MarkdownTOC -->

- jarvis
- nomadic
    - Features
    - Setup
        - Installation
        - Configuration
        - The Daemon
        - Custom CSS
    - Usage
        - Browsing notes
        - Searching notes
        - Adding other files (images, etc)
        - Presentations(TODO)
        - Tips
    - Development
    - Screenshots
- util
    - Kindle Clippings Import
    - Evernote Import
- Acknowledgements

<!-- /MarkdownTOC -->



## jarvis

under construction



## nomadic

`nomadic` supports a simple directory structure of HTML, Markdown, txt, and pdf notes and any other files which may need to be referenced. `nomadic` provides an easier way of searching through and browsing those files through either the command line or a simple web interface.

![](screenshots/01.png)

For example:

```bash
notes
├── books
│   ├── first book note.pdf
│   ├── second book note.md
│   └── _resources
│       └── some image.png
├── programming
│   └── python guide.html
└── some note.md
```

The structure will be mapped to the website with the exact safe arrangement. You don't have to worry about specific inner format within different apps. There are only folders and files here.

Now I'm using `nomadic` with [Github](www.github.com) to keep notes synced across devices. Actually you can choose whatever cloud service you want to sync your notes. As it is, `nomadic` will be a decentralized note system.

Also, `nomadic` runs a small server for browsing files. With a little bit of configuration, you can deploy it on a real server.

---

### Features

* Supports **GitHub-Flavored** Markdown
* Supports **MathJax** syntax
* Supports **references to images** and other files, and will automatically
update those references if the files are moved
* **Full-text search** (across html, txt, markdown, and even pdf files)
* A **rich text editor** (in-browser) for dumping in web clippings (external images are automatically saved locally)
* The rich text editor can **convert and save HTML notes into Markdown**
* **Auto-recompiling of Markdown** notes and updating of whatever browser is
viewing the note (i.e. live-ish previews)
* Serves **a browsable site of all your notes**
* Complete **command-line interface**
* Export notes as portable **presentations**

Most features can work pretty well now. And I'm still working on new featrues that I may need in the future.

---

### Setup

#### Installation

```bash
$ git clone https://github.com/wdxtub/wkk.git
$ cd nomadic-source
$ pip install .

# Install front-end packages.
$ cd nomadic/server/assets/
$ bower install

# Build the highlight.js library.
$ cd static/vendor/highlight
$ npm install
# ...with all languages
$ node tools/build.js
# ...or with only specific languages
$ node tools/build.js python ruby javascript scala java bash http sql cs cpp css json objectivec xml markdown apache nginx
```

#### Configuration

`nomadic` checks for a configuration at `~/.nomadic`. If you
start `nomadic` without a config, one will be created for you.

For example:

```json
{
    "root": "~/Notes",
    "default_notebook": "books"
}
```

Whenever you change this file, you must restart
the `nomadic` daemon:

```bash
# Linux (Upstart)
$ sudo restart nomadic

# OSX (there might be a better way)
$ pkill -f nomadic-d
$ launchctl start com.nomadic
```

#### The Daemon

The daemon watches your notes directory and automatically updates the index as they change. It will also automatically update references to other notes as they change.

The daemon also runs a small server which allows for easy browsing/searching through notes as well as a quick way of previewing notes as you work on them.

##### Let `nomadic` daemon run automatically on startup

##### Linux (Upstart)

If you're on a Linux distro that uses Upstart, you can do:

```bash
$ sudo cp scripts/nomadic.conf /etc/init/nomadic.conf
```

Then you can start the daemon:

```bash
$ sudo start nomadic
```

##### OSX (Upstart)

If you're on OSX, you can do:

```bash
$ cp scripts/com.nomadic.plist ~/Library/LaunchAgents/com.nomadic.plist
```

Then you can start the daemon:

```bash
$ launchctl load ~/Library/LaunchAgents/com.nomadic.plist
```

#### Custom CSS

You can specify a custom stylesheet to override the default one. In your config, specify the path to that stylesheet:

```json
{
    ...
    "override_stylesheet": "~/path/to/my/styles.css"
    ...
}
```

---

### Usage
Run the `nomadic` daemon if it isn't running already.

```bash
$ nomadic-d
```

Primary interaction with `nomadic` is through
the command line.

```bash
$ nomadic --help

Usage: nomadic [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  browse               Browse through notes via a web browser.
  clean                Removes unreferenced resource folders from a...
  count                Get the number of notes.
  index                Update or reset the note index.
  new                  Create a new note.
  search               Search through notes.
```

#### Browsing notes
You can browse this notes site by running:

```bash
$ nomadic browse
```

which opens up the root directory ('notebook') in your default web browser.

You can immediately jump to a specific notebook by passing its name in:

```bash
$ nomadic browse economics
```

If the specified name matches multiple notebooks, you'll be given the option to select the right one.

#### Searching notes

The `nomadic` daemon will maintain a search index for your notes as you update them.

You can search through your notes by running:

```bash
$ nomadic search <query>
```

This will present a list of results, along with snippets where the keyword was found, for you to choose from.

`nomadic` can search through HTML, Markdown, txt, and pdf files.

#### Adding other files (images, etc)

If you are going to be referencing other files in your notes, you should put them in a directory called `_resources` in that note's notebook directory. `nomadic` recognizes these directories and handles them specially.

#### Presentations(TODO)

You can export a note to a presentation format pretty easily. For example:

```bash
$ nomadic export_presentation path/to/some_note.md ~/Desktop/
```

This compiles the note to the specified folder, copying over images. The presentation can be opened in any browser.

The compiled HTML includes a script which breaks the note into slides according to `<hr>` tags (specified in Markdown as `---`, `***`, or `___`). Slides resize to take up the full window height, and any slides that are too tall are automatically scaled down.

You can use the up/down arrow keys to navigate.

#### Tips

- You can view the 20 most recently modified notes using the `/recent/` path in the web browser.

### Development

```bash
$ git clone https://github.com/ftzeng/nomadic.git
$ cd nomadic
$ pip install --editable .
```

This installs the package locally, allowing you to work on it and test it easily.

To run the included tests:

```bash
$ pip install nose
$ nosetests test
```

### Screenshots

![blockquotes and images](screenshots/01.png)

![embedded pdfs](screenshots/02.png)

![you can copy and paste articles easily through the web editor](screenshots/03.png)

![highlighting support](screenshots/04.png)

![nice images](screenshots/05.png)

![code and mathjax galore](screenshots/06.png)

## util

As I have lots of mobile devices that generate notes(e.g. kindle). I need to make sure that they can be merged in to `WKK` with ease.

### Kindle Clippings Import

It's very easy to import notes from kindle clippings:

+ Make sure that `kindle.py` and `Import` folder are under the same directory.
+ Execute `python kindle.py` to import kindle clippings to folder `Notes/kindle`

You need to make sure the root of the Notes folder is correct.

### Evernote Import

You need one more step to import notes from evernote:

+ Export the notebooks you want to import to `WKK` with `html` format
+ Put the folder into `Import` folder
+ Execute `python evernote.py` to import evernote notes to folder `Notes/evernote`

You need to make sure the root of the Notes folder is correct.


## Acknowledgements

+ The CSS stylesheet used for the compiled notes is based on the one from [here](https://gist.github.com/tuzz/3331384).
+ The original nomadic version is based on [here](https://github.com/ftzeng/nomadic)
