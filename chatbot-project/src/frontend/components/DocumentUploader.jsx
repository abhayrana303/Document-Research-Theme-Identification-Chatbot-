import React, { useState } from 'react';

const DocumentUploader = ({ onUpload }) => {
    const [selectedFiles, setSelectedFiles] = useState(null);
    const [uploadStatus, setUploadStatus] = useState('');

    const handleFileChange = (event) => {
        setSelectedFiles(event.target.files);
    };

    const handleUpload = async () => {
        if (!selectedFiles) {
            setUploadStatus('Please select files to upload.');
            return;
        }
        const formData = new FormData();
        for (let i = 0; i < selectedFiles.length; i++) {
            formData.append('files', selectedFiles[i]);
        }
        try {
            const response = await fetch('/upload/', {
                method: 'POST',
                body: formData,
            });
            if (response.ok) {
                setUploadStatus('Documents uploaded successfully!');
                if (onUpload) onUpload();
            } else {
                setUploadStatus('Failed to upload documents.');
            }
        } catch (error) {
            setUploadStatus('An error occurred during upload.');
        }
    };

    return (
        <div className="document-uploader">
            <input type="file" multiple onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload Documents</button>
            {uploadStatus && <p>{uploadStatus}</p>}
        </div>
    );
};

export default DocumentUploader;