import numpy as np
import mne
import matplotlib
matplotlib.use('TkAgg',force=True)
import matplotlib.pyplot as plt
import os

# sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = r"C:\Users\pd_user\Documents\BrainAccessData\subj-1_ses-S001_task-test1_run-001_20241116_124653_eeg_BA_MINI_026_6be9d3d9-5f9f-4e6f-9b68-5d7eae946ebb-raw.fif"
raw = mne.io.read_raw_fif(sample_data_raw_file)

# raw.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)
# raw.plot(duration=5, n_channels=30)
n_time_samps = raw.n_times
time_secs = raw.times
ch_names = raw.ch_names
n_chan = len(ch_names)  # note: there is no raw.n_channels attribute
print(
    f"the (cropped) sample data object has {n_time_samps} time samples and "
    f"{n_chan} channels."
)
print(f"The last time sample is at {time_secs[-1]} seconds.")
print("The first few channel names are {}.".format(", ".join(ch_names[:3])))
print()  # insert a blank line in the output

# some examples of raw.info:
print("bad channels:", raw.info["bads"])  # chs marked "bad" during acquisition
print(raw.info["sfreq"], "Hz")  # sampling frequency
print(raw.info["description"], "\n")  # miscellaneous acquisition info


sampling_freq = raw.info["sfreq"]
start_stop_seconds = np.array([11, 13])
start_sample, stop_sample = (start_stop_seconds * sampling_freq).astype(int)
channel_index = 3
# raw_selection = raw[channel_index, start_sample:stop_sample]
raw_selection = raw[channel_index, :]
print(raw_selection)

print(raw.info)

x = raw_selection[1]
y = raw_selection[0].T
plt.plot(x, y)

plt.show()

print("done")