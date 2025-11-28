import React from 'react';
import { api } from '../api/client';
import { FileText, Download } from 'lucide-react';

const Reports = () => {
    const generateReport = async () => {
        try {
            const response = await api.generatePdfReport();
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.download = 'ai_news_report.pdf';
            link.click();
        } catch (error) {
            console.error("Report generation failed:", error);
        }
    };

    return (
        <div className="min-h-screen p-8 bg-gradient-to-b from-[#050816] via-[#0e0a2a] to-[#050816] text-white">
           
            <div className="max-w-6xl mx-auto mb-10">
                <h1 className="text-4xl font-semibold tracking-tight">Reports</h1>
                <p className="text-white/60 text-sm mt-1">Download detailed AI analytics and system summaries.</p>
            </div>

            <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

                {/* Card */}
                <div className="glass-card bg-white/90 border border-white/10 rounded-2xl p-8 shadow-xl hover:shadow-primary/10 transition-all">
                    <div className="w-14 h-14 bg-primary/10 rounded-xl flex items-center justify-center text-primary mb-6">
                        <FileText size={28} />
                    </div>

                    <h3 className="text-xl font-semibold text-gray-900 mb-2">Daily Performance Report</h3>
                    <p className="text-gray-600 text-sm mb-6">
                        Contains classification accuracy, RAG results, system status, and activity logs.
                    </p>

                    <button
                        onClick={generateReport}
                        className="w-full py-3 bg-primary text-white rounded-xl hover:bg-primary/90 transition-all flex items-center justify-center gap-2 shadow-md shadow-primary/40"
                    >
                        <Download size={20} />
                        <span>Download Report</span>
                    </button>
                </div>
            </div>
        </div>
    );
};

export default Reports;
