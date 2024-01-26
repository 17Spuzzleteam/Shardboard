## M-Board

[![codecov](https://codecov.io/gh/cardinalitypuzzles/cardboard/branch/master/graph/badge.svg)](https://codecov.io/gh/cardinalitypuzzles/cardboard)

M-Board is the 17th Shard's fork of [Cardboard](https://github.com/cardinalitypuzzles/cardboard), which helps teams coordinate solving [puzzlehunts](https://en.wikipedia.org/wiki/Puzzle_hunt). It is named after [M-Bot](https://github.com/Moonrise55/Mbot), our beloved companion-slash-partner-in-spacetime. M-Board manages and organizes puzzles, keeps track of team members, integrates with other solving tools, and more.

Most of this documentation has been maintained from the original Cardboard docs, with changes specific to the 17th Shard's hunt workflow as appropriate.

For help **using M-Board as a solver**, see [here](user-guide.md).

For help **setting M-Board up for a hunt**, see [here](new-hunt-setup.md).

For information about **development**, see the [dev guide](dev-guide.md).

### Features

* Seamlessly supports (almost) any puzzle hunt structure
* Create and assign tags to puzzles
* Quickly search and filter on puzzle names, rounds, and tags
* Remote-friendly! Real-time display of what everyone's working on at any time

### Integrations

#### Google Sheets

* Creates a Google Sheet for new puzzles automatically
* Real-time display of how active each puzzle's sheet is, and who's currently editing it
* Cleans up unneeded sheets and automatically transfers answers into metapuzzle sheets

#### Discord
* Creates, manages, and archives Discord voice + text channels for each puzzle
* Announces new puzzles in a central channel
* Keeps tags synced with Discord roles
* Automatically `@mention` interested hunters when a puzzle with a specific tag is unlocked

### Other

* Chrome extension to add new puzzles with one click
* Supports answer queues (anyone can submit answers to the queue, but only admins can mark them as correct)
* Dark and light modes
