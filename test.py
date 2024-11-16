import numpy as np
import mne


sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = r"C:\pd\Projects\_test\NeuroHackhaton\sample_data\subj-1_ses-S001_task-test1_run-001_20241116_124653_eeg.db"
raw = mne.io.read_raw_fif(sample_data_raw_file)