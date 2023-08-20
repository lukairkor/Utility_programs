#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 14:44:38 2022
# calculate cylinder volume
# draw cylinder
@author: lukas
"""
import math
import matplotlib.pyplot as plt
import numpy as np


def calculate_volume(h, r):
    # cm^2
    sur_are = math.pi * (r ** 2)
    # cm^3
    volu = sur_are * h
    # in cubic meter
    volu = volu * 10 ** -6
    # in liter
    volu = round((volu * 1000), 3)
    # show result
    print(volu, "l")
    return volu


def prepare_figure():
    # prepare figure
    # plt.rcParams["figure.figsize"] = plt.rcParamsDefault["figure.figsize"]
    fig = plt.figure(figsize=(6, 6), dpi=144)
    plt.rc('xtick', labelsize=12)
    ax = fig.add_subplot(111, projection='3d')
    ax.grid(True)
    ax.set_title('CYLINDER VOLUME', fontsize=14)
    return fig, ax


def constuct_cylinder(fig, ax):
    # points vectors
    x = np.linspace(-1, 1, 100)
    z = np.linspace(0, h, 100)

    # points matrices
    xc, zc = np.meshgrid(x, z)
    # surface equetion
    yc = np.sqrt(1 - xc ** 2)

    # Draw both sides of the cylinder
    ax.plot_surface(xc * r, yc * r, zc, alpha=0.6)
    ax.plot_surface(xc * r, -yc * r, zc, alpha=0.6)


def draw_on_ax(h, r):
    calculate_volume(h, r)
    fig, ax = prepare_figure()
    constuct_cylinder(fig, ax)
    volu = calculate_volume(h, r)
    # draw volume vaule on a figure
    ax.text2D(0.65, 0.9, "vol = " + str(volu) + " l", transform=ax.transAxes,
              color="green", fontsize=14)
    # 
    x_value = [0, r]
    y_value = [0, 0]
    z_value = [0, 0]
    ax.plot(x_value, y_value, z_value)
    ax.text2D(0.55, 0.5, "h = " + str(h) + " cm", transform=ax.transAxes,
              color="green", fontsize=14)
    x_value = [0, 0]
    y_value = [0, 0]
    z_value = [0, h]
    ax.plot(x_value, y_value, z_value)
    ax.text2D(0.5, 0.2, "r = " + str(r) + " cm", transform=ax.transAxes,
              color="green", fontsize=14)
    ax.set_xlabel("x_value")
    ax.set_ylabel("y_value")
    ax.set_zlabel("z_value")
    fig.savefig('cylinder_volume.png')


# in cm
h = 200
r = 50

draw_on_ax(h, r)
