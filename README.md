# PINE64 Collaborative Community Updates

This repository contains the drafts and finished posts for PINE64 community
updates, as authored by the community in a collaborative manner. Anyone is able
to contribute.


## Contributing

Contributing is done by submitting either short sentences, whole paragraphs or
even just a single link into `ingress/<date>/todo.md`. Accompanying images may
also be submitted to the `ingress/<date>/` directory.

Either dump your contributions at the top of the file in a new paragraph or add
a new section with a `## Heading` at the bottom of the file, don't worry about
formatting but try to use markdown where sensible.

When contributing images, try to contribute them in the best available quality,
but strip them of any EXIF data you don't want to be public (e.g. with exiftool)
as the repository itself is public. Processing the images into a form
appropriate for the blog and/or update videos is done by the maintainers and
video editors.

If you'd like to submit an entire section attributed to you specifically,
please create a new section with a `## Heading` at the bottom of the file and
follow it with `(By <your preferred name here>)`, for example
`## PineCar's Tire Pressure Conundrum (By CounterPillow)`. In such a section,
you may use first person pronouns (e.g. "I bought the Pinecorn"). Editing of
such sections by the maintainers will respect your author voice, but may include
editorial decisions such as shortening of sections, rewording for flow or
clarification of certain terms.


## The Process

The maintainers/editors of this repository will periodically take items from
`todo.md` and write them as well formatted prose into the
`final/<date>/post.md` file. This file is as closely representative to the
final post to be published as is possible.

Items processed from `ingress/<date>/todo.md` will be moved to
`ingress/<date>/done.md`.

Dates are given in `YYYY-MM` format.

Contributors will be credited in each update post by their account name, if
you'd like to be credited under a different handle please indicate this in your
merge request.

### For Editors

Please use American English spelling in the final written article (e.g. "color"
instead of "colour".)

Begin with a TL;DR of all the sections, then a Housekeeping section for anything
meta including FOSDEM, and then a Newsflash section for any small news items
worth only about a paragraph or two. Then follow this with sections either
dedicated to specific devices or to major topics.

Avoid needless editorialising, as the community update should be a product of
the community's voice, not the editor's. Named community members may express
their opinions in sections specifically attributed to them in the title,
where they may also use first person pronouns. Otherwise, always write in third
person, even when covering yourself.

Create a lead image that is relevant to at least one of the covered major
topics. The lead image should be 1920 by 1080 pixels in resolution or a multiple
thereof. Its filename should be "lead", to avoid any confusion.

Include the following text at the end of the opening section:

> N.B. Comments on the blog post need to be in English and follow our
> [Community Rules and Code of Conduct](https://forum.pine64.org/showthread.php?tid=13209).

When finalising and publishing a community update, maintainers will add any
"embargoed" product news from Pine Store to the post, publish the post on the
PINE64 blog and create a new annotated git tag of the form `vYYYY-MM` reflecting
the year and month of the update. A new directory for next month's community
update is then created.


## Schedule

We aim to have posts out by **the 15th of every month**. Please submit any
material you'd like to have included **2 days before this deadline**. Late
submissions may be included in the next month's community update instead.


## Licensing

By submitting to this repository, you agree that you have the necessary rights
to submit your contributions and grant us a perpetual, irrevocable, royalty-free
license to adapt, feature and distribute your submission on or through the
PINE64.org website as part of a community update, as well as produce and
distribute video and audio adaptations of your contributions for the purpose of
creating PINE64 community update videos and PINE64 podcasts.

You also grant a perpetual, irrevocable, royalty-free license to have your
contribution be distributed as part of this repository, and have it be modified
or adapted into different forms for the purposes of creating PINE64 community
updates.

Contributors retain the copyrights to their own contributions.
