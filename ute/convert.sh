BASE_DIR=/raw_dicom    # location of raw data folder
T1_FOLDER=t1w_3d_MPRAGE            # dicom folder containing anatomical scan
DATA_DIR=/data        # location of output folder

# not as efficientas nypipe's dcm2nii

do
    mri_convert $BASE_DIR/$T1_FOLDER/ name .dcm    $DATA_DIR/sub0$id/struct.nii.gz
done
