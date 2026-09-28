#! /usr/bin/env python
#-*-coding: utf-8 -*-

#import re
import sys
import os
import tarfile
import shutil

from pathlib import Path
from PIL import Image
import glob
from itertools import islice


def launchConversion(args):
    walkToConvert = '/eos/project-c/cmsweb/www/egamma/validation/Electrons/Releases'
    print('walkToConvert = ' + walkToConvert)
    print('walkToConvert (absolute) = ' + os.path.abspath(walkToConvert))

    chemin = Path(walkToConvert)
    number = 0
    dirContent1 = [d.name for d in chemin.iterdir() if d.is_dir() and d.name[0].isdigit()]
    for folder1 in dirContent1:
        chemin2 = chemin / folder1
        nb = int(folder1[:2])
        dirContent2 = [d.name for d in chemin2.iterdir() if d.is_dir()]
        for folder2 in dirContent2:
            if (nb >= 14) :
                print(f'numero : {nb}')
                print(f"\n\033[1m{'*' * 2} {folder1} {'*' * 2}\033[0m / \033[1;32m{'*' * 2} {folder2} {'*' * 2}\033[0m")
                chemin3 = chemin2 / folder2
                dirContent3 = [d.name for d in chemin3.iterdir() if d.is_dir()]
                for folder3 in dirContent3:
                    number += 1
                    print(f"            \033[1;34m{'*' * 10} {folder3} {'*' * 10}\033[0m")
                    chemin4 = chemin3 / folder3
                    dirContent4 = [d.name for d in chemin4.iterdir()]
                    required = ['config_reference.txt', 'config_target.txt', 'definitions.txt', 'pngs']
                    missing = [f for f in required if not (chemin4 / f).exists()]
                    if missing:
                        print(dirContent4)
                        print(f"\033[1;31mManquants : {missing}\033[0m")
                    
                    
                    #if ('pngs' in missing or not any((chemin4 / "pngs").iterdir())):
                    #if ('pngs' in missing ):
                    Path(chemin4/"pngs").mkdir(parents=True, exist_ok=True)
                    src = Path(chemin4/'gifs')
                    dst = Path(chemin4/'pngs')
                    if os.path.isdir(src): # teste si /gifs/ existe
                        print(src)
                        print(dst)
                        dst.mkdir(exist_ok=True)

                        for f in src.glob('*.gif'):
                            img = Image.open(f)
                            img.save(dst / f.with_suffix('.png').name)
                        with tarfile.open(chemin4/"gifs.tar.gz", "w:gz") as tar:
                            tar.add(src, arcname="gifs")
                        if os.path.getsize(chemin4/"gifs.tar.gz") > 0:
                            shutil.rmtree(src)
                        else:
                            print("Archive vide, suppression annulée.")
                    else:
                        print('no gifs folder.')
                    #''''''

                    if ('definitions.txt' in missing):
                        print('definitions.txt is missing')
                        if 'index.html' in dirContent4:
                            if (chemin4/"index.html").stat().st_size == 0:
                                print("\033[1;33mindex.html vide, skip\033[0m")
                            else:
                                with open(chemin4/"index.html") as f:
                                    lignes = list(islice(f, 4, 10))
                                print(f'nb lignes : {len(lignes)}')
                                del lignes[1:3]
                                print(f'nb lignes : {len(lignes)}')
                                lignes = [l.rstrip('\n') for l in lignes]
                                lignes = [l.replace('<b>', '').replace('</b>', '') for l in lignes]
                                lignes = [l.replace('<h1>', '').replace('</h1>', '') for l in lignes]
                                lignes = [l.replace('<title>', '').replace('</title>', '') for l in lignes]
                                lignes = [l.replace('<p>', '').replace('</p>', '') for l in lignes]
                                lignes = [l.replace('</a>', '').replace('</font>', '') for l in lignes]
                                lignes = [l.replace("<font color='blue'>", '').replace('<font color=\'red\'>', '') for l in lignes]
                                lignes = [l.replace('<br>', '').replace('<a href=', '') for l in lignes]
                                print(lignes)
                                newTewt = lignes[0].replace(' ', '') + "\n"
                                t1 = lignes[1].split(":")
                                p11 = (t1[0].lstrip()).split(' ')
                                t2 = lignes[2].split(":")
                                p21 = (t2[0].lstrip()).split(' ')
                                newTewt += p11[0] + "\n"
                                newTewt += p11[1] + "\n"
                                newTewt += t1[1].lstrip() + "\n"
                                newTewt += p21[0] + "\n"
                                newTewt += p21[1] + "\n"
                                newTewt += t2[1].lstrip() + "\n"
                                t3 = lignes[3].split(' histograms ')
                                t31 = 'C' + t3[0].split('  C')[1]
                                t32 = 'C' + t3[1].split('  C')[1]
                                newTewt += t31 + "\n"
                                newTewt += t32 + "\n"
                                newTewt += "\n" + "config_target.txt" + "\n"
                                print(newTewt)
                                with open(chemin4/"definitions.txt", 'w+') as file_o:
                                    file_o.write(newTewt)
                                file_o.close()
                        else:
                            print('no index.html && no definitions.txt')
                            continue
    print(f'il y a {number} repertoires.')
   

if __name__ == "__main__":

    launchConversion(sys.argv)
    print('fin')
