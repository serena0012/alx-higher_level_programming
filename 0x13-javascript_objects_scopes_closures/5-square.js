#!/usr/bin/node
module.experts = class square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
