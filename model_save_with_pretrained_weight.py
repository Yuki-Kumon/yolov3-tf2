# -*- coding: utf-8 -*-

"""
tensorflow.jsへのコンバート用にkerasモデルを書き出す。
Author :
    Yuki Kumon
Last Update :
    2019-08-03
"""

import time
from absl import app, flags, logging
from absl.flags import FLAGS
import cv2
import numpy as np
import tensorflow as tf
from yolov3_tf2.models import (
    YoloV3, YoloV3Tiny
)
from yolov3_tf2.dataset import transform_images
from yolov3_tf2.utils import draw_outputs

flags.DEFINE_string('classes', './data/coco.names', 'path to classes file')
flags.DEFINE_string('weights', './checkpoints/yolov3.tf',
                    'path to weights file')
flags.DEFINE_boolean('tiny', False, 'yolov3 or yolov3-tiny')
flags.DEFINE_integer('size', 416, 'resize images to')
flags.DEFINE_string('image', './data/girl.png', 'path to input image')
flags.DEFINE_string('output', './output.jpg', 'path to output image')
flags.DEFINE_string('save_name', '', 'path to output model')


def main(_argv):
    if FLAGS.tiny:
        yolo = YoloV3Tiny()
    else:
        yolo = YoloV3()

    yolo.load_weights(FLAGS.weights)
    logging.info('weights loaded')

    # class_names = [c.strip() for c in open(FLAGS.classes).readlines()]
    # logging.info('classes loaded')

    # model save at root
    if FLAGS.tiny:
        save_name = './output/yolov3-tf2-tiny.h5'
    else:
        save_name = './output/yolov3-tf2.h5'
    if FLAGS.save_name:
        save_name = FLAGS.save_name
    yolo.save(save_name)
    logging.info('model is saved as {}'.format(save_name))
    del yolo


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
