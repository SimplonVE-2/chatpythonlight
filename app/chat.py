#!/usr/bin/env python3
#coding: utf-8

import argparse
import json
import os
import rethinkdb as rdb

from flask import Flask, g, jsonify, render_template, request, abort

from rethinkdb.errors import RqlRuntimeError, RqlDriverError

app = Flask(__name__)


#plein de truc a remplir la

if __name__ == '__main__':
    app.debug = True
    app.run()
