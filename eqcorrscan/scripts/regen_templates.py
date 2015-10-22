#!/usr/bin/env python
"""
Script to re-gernate templates from the originally defined templates of varying
lengths, and enable stacking.

Copyright 2015 Calum Chamberlain

This file is part of EQcorrscan.

    EQcorrscan is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EQcorrscan is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with EQcorrscan.  If not, see <http://www.gnu.org/licenses/>.

"""
import glob, os, sys
# sys.path.append('/home/calumch/my_programs/Building/EQcorrscan')
sys.path.append('/Volumes/GeoPhysics_09/users-data/chambeca/my_programs/Building/EQcorrscan')
templates=glob.glob('templates/adaptive_tremor/*.ms')
datasource='/Volumes/GeoPhysics_09/users-data/chambeca/SAMBA_archive/day_volumes_S/'
GeoNet='/Volumes/GeoPhysics_09/users-data/chambeca/Alpine_Fault_SAC/SAC_resampled/'
length1=3.0
length2=6.0
out2='templates/6sec_templates'
length3=12.0
out3='templates/12sec_templates'
# Lengths in seconds, length1 should be the original length
# Lengths will be generated by ading extra data in equal amounts to the front
# and back of templates

from obspy import read, Stream
from utils import clustering, stacking
from utils import EQcorrscan_plotting as plotting
from par import template_gen_par as defaults
from core import template_gen
from utils.Sfile_util import PICK
import numpy as np
import matplotlib.pyplot as plt

templates.sort()
# f=open('regen_template.err','w')
# for tfile in templates:
    # # Check to see if the work has already been done
    # if glob.glob(out2+'/'+tfile.split('/')[-1]) and \
       # glob.glob(out3+'/'+tfile.split('/')[-1]):
        # print 'Already worked on: '+tfile.split('/')[-1]
        # continue
    # template=read(tfile)
    # picks=[]
    # if 'original_data' in locals():
        # del original_data
    # i=0
    # for tr in template:
        # # Perform check on channel and station names
        # if tr.stats.station=='COSA' and tr.stats.channel=='S2':
            # tr.stats.chanel='SE'
        # if tr.stats.station=='COSA' and tr.stats.channel=='S1':
            # tr.stats.channel='SN'
        # if tr.stats.network=='AF':
            # if not 'original_data' in locals():
                # original_data=read(datasource+tr.stats.starttime.datetime.strftime('Y%Y/R%j.01')+\
                               # '/'+tr.stats.station+'.'+tr.stats.network+'.*'+\
                               # tr.stats.channel[-1]+'.'+\
                               # tr.stats.starttime.datetime.strftime('%Y.%j'))
            # else:
                # original_data+=read(datasource+tr.stats.starttime.datetime.strftime('Y%Y/R%j.01')+\
                               # '/'+tr.stats.station+'.'+tr.stats.network+'.*'+\
                               # tr.stats.channel[-1]+'.'+\
                               # tr.stats.starttime.datetime.strftime('%Y.%j'))
        # else:
            # if not 'original_data' in locals():
                # original_data=read(GeoNet+tr.stats.starttime.datetime.strftime('%Y%m%d')+\
                               # '/*'+tr.stats.station+'.*'+\
                               # tr.stats.channel[-1]+'.SAC')
            # else:
                # original_data+=read(GeoNet+tr.stats.starttime.datetime.strftime('%Y%m%d')+\
                               # '/*'+tr.stats.station+'.*'+\
                               # tr.stats.channel[-1]+'.SAC')
        # picks.append(PICK(station=original_data[i].stats.station,
                        # channel=original_data[i].stats.channel[0]+original_data[i].stats.channel[2],
                        # impulsivity='E', phase='S',
                        # weight='3', polarity='',
                        # time=tr.stats.starttime,
                        # coda='', amplitude='', peri='',
                        # azimuth='', velocity='', AIN='', SNR='',
                        # azimuthres='', timeres='',
                        # finalweight='', distance='',
                        # CAZ=''))
        # i+=1
    # original_data.merge()
    # print 'I have '+str(len(original_data))+' traces of data'
    # print 'For which I have '+str(len(picks))+' picks'

    # second_gen_template=template_gen._template_gen(picks, original_data,\
                                                           # length2, 'all')
    # third_gen_template=template_gen._template_gen(picks, original_data,\
                                                           # length3, 'all')
    # # Check that there actually is data for every channel
    # missing_data=False
    # for tr in second_gen_template:
        # try:
            # tr.split()
            # if not 'temp' in locals():
                # temp=Stream(tr)
            # else:
                # temp+=tr
        # except:
            # print 'No data for: '+tr.stats.station+' '+tr.stats.channel
            # missing_data=True
    # second_gen_template=temp
    # del temp

    # for tr in third_gen_template:
        # try:
            # tr.split()
            # if not 'temp' in locals():
                # temp=Stream(tr)
            # else:
                # temp+=tr
        # except:
            # print 'No data for: '+tr.stats.station+' '+tr.stats.channel
            # missing_data=True
    # third_gen_template=temp
    # del temp

    # if missing_data:
        # for tr in template:
            # for x in second_gen_template:
                # if tr.stats.station==x.stats.station and tr.stats.channel==x.stats.channel:
                    # if not 'temp' in locals():
                        # temp=Stream(tr)
                    # else:
                        # temp+=tr
        # template_out=temp
        # del temp
        # print 'Overwriting old template that had spurious data'
        # # template_out.plot()
        # template_out.write(tfile, format='mseed')

    # # Write out the templates
    # if not os.path.isdir(out2):
        # os.makedirs(out2)
    # if not os.path.isdir(out3):
        # os.makedirs(out3)
    # try:
        # second_gen_template.write(out2+'/'+tfile.split('/')[-1], format='mseed')
    # except NotImplementedError:
        # second_gen_template=second_gen_template.split()
        # second_gen_template.write(out2+'/'+tfile.split('/')[-1], format='mseed')
        # f.write('Had to split: '+out2+'/'+tfile.split('/')[-1])
    # print 'Written '+str(length2)+' second long template to: '+out2+'/'+tfile.split('/')[-1]
    # try:
        # second_gen_template.write(out2+'/'+tfile.split('/')[-1], format='mseed')
    # except NotImplementedError:
        # second_gen_template=second_gen_template.split()
        # second_gen_template.write(out2+'/'+tfile.split('/')[-1], format='mseed')
        # f.write('Had to split: '+out2+'/'+tfile.split('/')[-1])
    # print 'Written '+str(length3)+' second long template to: '+out3+'/'+tfile.split('/')[-1]
# f.close()

# Compute the stacks of the original templates
template_streams=[]
templates=[read(tfile) for tfile in templates]
good_templates=[]
print 'Read in '+str(len(templates))+' templates'
for template in templates:
    nanin=False
    for tr in template:
        if np.any(np.isnan(tr.data)):
            tr.data=np.nan_to_num(tr.data)
        if np.all(tr.data==0):
            template.remove(tr)
            # Remove empty traces
    if not nanin:
        good_templates.append(template)
print 'I have '+str(len(good_templates))+' without nans'


for template in good_templates:
    correct_length=True
    for tr in template:
        if not len(tr.data)==120:
            correct_length=False
    if correct_length:
        template_streams.append(template)
print 'I have '+str(len(template_streams))+' templates of 120s length'

fivesta_templates=[]
# Extract five stations with highest amplitude
for template in template_streams:
    stations=list(set([tr.stats.station for tr in template]))
    if len(stations) < 5:
        continue
    amps=[]
    for station in stations:
        st=template.select(station=station)
        amp=0
        for tr in st:
            amp+=np.max(np.abs(tr.data))
        amps.append((station, amp))
    amps.sort(key=lambda tup:tup[1])
    stations=[a[0] for a in amps[-5:]]
    avamp=np.mean([a[1] for a in amps[-5:]])
    for sta in stations:
        if not 'fivesta_template' in locals():
            fivesta_template=template.select(station=sta)
        else:
            fivesta_template+=template.select(station=sta)
    fivesta_templates.append((fivesta_template, avamp))
    del fivesta_template

fivesta_templates.sort(key=lambda tup:tup[1])
template_streams=[t[0] for t in fivesta_templates]
# # Extract the highest 100 amplitude events
# template_streams=[t[0] for t in fivesta_templates[-100:]]

# for template in template_streams:
    # template.write('templates/top_100/'+str(template[0].stats.starttime)+'.ms', format='MSEED')

groups=clustering.group_delays(template_streams)
ID=1
from collections import Counter

for group in groups:
   if len(group) >1:
       print 'Group '+str(ID)+' of '+str(len(groups))+' has '+str(len(group))+' templates'
       # template_stack=stacking.PWS_stack(group, 1.2)
       template_stack=stacking.linstack(group)
        # template_stack.filter('bandpass', freqmin=defaults.lowcut, freqmax=defaults.highcut)
        # template_stack.plot(size=(800,600), equal_scale=False)
       template_stack.write('templates/pan_templates/brightness_group'+str(ID), format='mseed')
   ID+=1
