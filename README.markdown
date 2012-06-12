# LastTitle Plugin for Supybot

The goal of this plugin is to make the supybot html title feedback less
terribad.

## Installation

Is like any other plugin.  Don't forget to update your config =)

## Dependencies

lxml, which should be installable from pip or easy\_install, or directly from
Pypi.

## Usage

After a link has been submitted, a user may enter the command ```<char>lt```,
where <char> is whatever character should precede commands on your personal
setup.  This will either give an error that no title is available, print that
the link is actually a file of a specific file type, or report the title to the
user who asked for it.

