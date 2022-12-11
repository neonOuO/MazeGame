from os import walk
import pygame
import csv


def import_csv_layout(path):
    with open(path) as csvfile:
        map_list = []
        reader = csv.reader(csvfile)
        for line in reader:
            map_list.append(line)
    return map_list


def import_folder(path):
    surface_list = []
    for _, _, img_files in walk(path):
        for img in img_files:
            full_path = path + '/' + img
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)
    return surface_list
