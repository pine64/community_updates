#!/usr/bin/env python3
import argparse
import re
import sys
import mistune


def load_dictionary(d_path):
    with open(d_path, 'r') as f:
        d = dict([(line.lower().strip(), None) for line in f])
    return d


def post_to_words(post):
    r = re.compile(r'\b[a-zA-Z0-9\'\-]+\b')
    l = []
    for word in re.findall(r, post):
        l.append(word.strip(':;,."[]()'))
    return l


def lint_english_version(post, ae_d, be_d):
    ret = 0
    for i, l in enumerate(post.splitlines(keepends=True)):
        words = post_to_words(l)
        for w in words:
            if w in be_d:
                if not w in ae_d:
                    print("Warning: Line {}: '{}' is a possible British English word!"
                          .format(i+1, w))
                    ret = 2
    return ret


def lint_markdown_headers(md):
    num_top_headings = 0
    ret = 0

    for tok in md:
        if tok["type"] == "heading":
            if tok["attrs"]["level"] == 1:
                num_top_headings += 1
                heading = tok["children"][0]["raw"]
                if not heading.istitle():
                    print("Warning: Heading '{}' is not title cased!".format(heading))
                    ret = 2

    if num_top_headings != 1:
        print("Warning: Too many/few top level headings! ({})".format(num_top_headings))
        return 2

    return ret


def main():
    post = None
    ret = 0
    exit_status = 0
    parser = argparse.ArgumentParser(
        description="A linter for PINE64 blog posts"
    )
    parser.add_argument('filename')
    parser.add_argument('--american-dict',
                        default="/usr/share/dict/american-english",
                        help="path to line-delimited list of American English words.")
    parser.add_argument('--british-dict',
                        default="/usr/share/dict/british-english",
                        help="path to line-delimited list of British English words.")
    args = parser.parse_args()

    try:
        ae_d = load_dictionary(args.american_dict)
        be_d = load_dictionary(args.british_dict)
    except FileNotFoundError as e:
        print("Couldn't find dictionary '{}'.".format(e.filename))
        return 1
    try:
        with open(args.filename, 'r') as f:
            post = f.read()
    except FileNotFoundError as e:
        print("Couldn't find post '{}'.".format(e.filename))

    ret = lint_english_version(post, ae_d, be_d)
    if ret:
        exit_status = ret

    markdown = mistune.create_markdown(renderer=None)
    md = markdown(post)

    ret = lint_markdown_headers(md)
    if ret:
        exit_status = ret

    return exit_status


if __name__ == '__main__':
    sys.exit(main())
