BASE_DIR=/raw_dicom    # location of raw data folder
T1_FOLDER=t1w_3d_MPRAGE            # dicom folder containing anatomical scan
DATA_DIR=/data        # location of output folder




for id in $(seq -w 1 10)
do
    mri_convert $BASE_DIR/sub0$id/$T1_FOLDER/00001.dcm    $DATA_DIR/sub0$id/struct.nii.gz
done
