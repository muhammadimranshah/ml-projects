import { useEffect, useState } from "react";
import api from "../api/api";

function Sidebar() {

    const [file, setFile] = useState(null);
    const [documents, setDocuments] = useState([]);

    // ==========================
    // Load Documents
    // ==========================

    const loadDocuments = async () => {

        try {

            const response = await api.get("/documents");

            setDocuments(response.data);

        }

        catch (err) {

            console.log(err);

        }

    };

    // ==========================
    // Delete Document
    // ==========================

    const deleteDocument = async (id) => {

        const confirmDelete = window.confirm(
            "Are you sure you want to delete this PDF?"
        );

        if (!confirmDelete) return;

        try {

            await api.delete(`/documents/${id}`);

            alert("Deleted Successfully");

            loadDocuments();

        }

        catch (err) {

            console.log(err);

            alert("Delete Failed");

        }

    };

    // ==========================
    // Load Documents on Start
    // ==========================

    useEffect(() => {

        loadDocuments();

    }, []);

    // ==========================
    // Upload PDF
    // ==========================

    const uploadFile = async () => {

        if (!file) {

            alert("Please select a PDF");

            return;

        }

        const formData = new FormData();

        formData.append("file", file);

        try {

            await api.post(
                "/documents/upload",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                }
            );

            alert("PDF Uploaded Successfully");

            setFile(null);

            loadDocuments();

        }

        catch (err) {

            console.log(err);

            alert("Upload Failed");

        }

    };

    return (

        <div className="sidebar">

            <h2>KnowledgePilot AI</h2>

            <hr />

            <h3>Upload PDF</h3>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) => setFile(e.target.files[0])}
            />

            <br />
            <br />

            <button onClick={uploadFile}>
                Upload PDF
            </button>

            <hr />

            <h3>Uploaded PDFs</h3>

            {

                documents.length === 0 ? (

                    <p>No PDFs Uploaded</p>

                ) : (

                    documents.map((doc) => (

                        <div
                            key={doc.id}
                            style={{
                                display: "flex",
                                justifyContent: "space-between",
                                alignItems: "center",
                                padding: "10px",
                                marginBottom: "10px",
                                border: "1px solid #ddd",
                                borderRadius: "8px"
                            }}
                        >

                            <span>
                                📄 {doc.filename}
                            </span>

                            <button
                                onClick={() => deleteDocument(doc.id)}
                                style={{
                                    background: "red",
                                    color: "white",
                                    border: "none",
                                    borderRadius: "4px",
                                    cursor: "pointer",
                                    padding: "5px 10px"
                                }}
                            >
                                Delete
                            </button>

                        </div>

                    ))

                )

            }

        </div>

    );

}

export default Sidebar;