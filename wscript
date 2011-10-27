#! /usr/bin/env python

top = '.'
out = 'build'
children = [ 'example' ]

def configure(ctx):
    ctx.recurse(children)

def build(ctx):
    ctx.recurse(children)

def install(ctx):
    ctx.recurse(children)

