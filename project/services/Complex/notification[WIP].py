from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import os, sys

import requests
from invokes import invoke_http
import json
from os import environ

