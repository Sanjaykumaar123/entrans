import React, { useEffect, useState } from 'react';
import { api } from '../api/client';
import {
    Download,
    Database,
    Zap,
    BarChart3,
    FileText,
    Activity,
    MessageSquare
} from 'lucide-react';

const Dashboard = () => {
    const [metrics, setMetrics] = useState([]);
    const [recentActivity, setRecentActivity] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchData();
        const interval = setInterval(fetchData, 3000);
        return () => clearInterval(interval);
    }, []);

    const fetchData = async () => {
        try {
            const [metricsRes, activityRes] = await Promise.all([
                api.getMetrics(),
                api.getRecentActivity()
            ]);

            if (metricsRes.data.status === 'success') {
                setMetrics(metricsRes.data.metrics);
            }

            if (activityRes.data.status === 'success') {
                setRecentActivity(activityRes.data.activities);
            }

            setLoading(false);
        } catch (error) {
            console.error("Failed to fetch dashboard data:", error);
            setLoading(false);
        }
    };

    const downloadReport = async () => {
        try {
            const response = await api.generatePdfReport();
            const blob = new Blob([response.data], { type: 'application/pdf' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'report.pdf';
            a.click();
        } catch (error) {
            console.error("PDF download failed:", error);
        }
    };

    const getIcon = (iconName) => {
        const icons = {
            'Database': Database,
            'Zap': Zap,
            'BarChart3': BarChart3,
            'FileText': FileText
        };
        const Icon = icons[iconName] || Database;
        return <Icon size={22} />;
    };

    const getModeIcon = (mode) => {
        if (mode === 'rag') {
            return <Database size={16} className="text-primary" />;
        }
        return <MessageSquare size={16} className="text-pink-500" />;
    };

    const getModeLabel = (mode) => {
        return mode === 'rag' ? 'RAG Search' : 'Chat';
    };

    return (
        <div className="min-h-screen p-8 bg-gradient-to-b from-[#050816] via-[#0e0a2a] to-[#050816] text-white">
            
            {/* Header */}
            <div className="flex items-center justify-between max-w-7xl mx-auto mb-10">
                <div>
                    <h1 className="text-4xl font-semibold tracking-tight">Dashboard</h1>
                    <p className="text-white/60 mt-1 text-sm">Real-time RAG performance and system analytics</p>
                </div>

                <button
                    onClick={downloadReport}
                    className="px-6 py-3 bg-primary rounded-xl hover:bg-primary/90 transition-all flex items-center space-x-2 text-white shadow-lg shadow-primary/40"
                >
                    <Download size={18} />
                    <span>Download Report</span>
                </button>
            </div>

            {/* Metrics */}
            <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
                {metrics.map((metric, idx) => (
                    <div
                        key={idx}
                        className="glass-card p-6 rounded-2xl border border-white/10 bg-white/90 backdrop-blur-xl 
                        hover:shadow-xl hover:shadow-primary/20 transition-all"
                    >
                        <div className="flex items-center justify-between mb-3">
                            <div className="p-3 rounded-xl bg-primary/10 text-primary shadow-sm">
                                {getIcon(metric.icon)}
                            </div>
                            <span className="text-xs text-emerald-600 font-medium">{metric.change}</span>
                        </div>
                        <h3 className="text-3xl font-semibold text-gray-900">{metric.value}</h3>
                        <p className="text-gray-600 text-sm">{metric.title}</p>
                    </div>
                ))}
            </div>

            <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8">
                
                {/* Recent Activity */}
                <div className="glass-card bg-white/90 border border-white/20 rounded-2xl p-6 backdrop-blur-xl shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <h3 className="text-xl font-semibold text-gray-900 flex items-center gap-2">
                            <Activity className="text-primary" />
                            Recent Activity
                        </h3>
                        <span className="flex items-center gap-2 text-xs text-gray-600">
                            <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
                            Live
                        </span>
                    </div>

                    {loading ? (
                        <div className="space-y-4">
                            {[1, 2, 3].map(i => (
                                <div key={i} className="h-14 bg-gray-200 rounded-xl animate-pulse"></div>
                            ))}
                        </div>
                    ) : recentActivity.length > 0 ? (
                        <div className="space-y-3 max-h-96 overflow-y-auto custom-scroll">
                            {recentActivity.map((activity, idx) => (
                                <div
                                    key={idx}
                                    className="p-4 bg-gray-100 rounded-xl border border-gray-200 hover:border-primary/40 transition-all"
                                >
                                    <div className="flex items-start justify-between">
                                        <div className="flex-1">
                                            <div className="flex items-center gap-2 mb-1">
                                                {getModeIcon(activity.mode)}
                                                <span className="text-xs font-medium text-gray-600">{getModeLabel(activity.mode)}</span>
                                            </div>
                                            <p className="text-gray-800 text-sm line-clamp-2">{activity.query}</p>
                                        </div>
                                        <span className="text-xs text-gray-500 ml-3">{activity.timestamp}</span>
                                    </div>
                                </div>
                            ))}
                        </div>
                    ) : (
                        <div className="text-center py-12 text-gray-400">
                            <Activity size={40} className="mx-auto opacity-40" />
                            <p>No activity yet. Start asking something!</p>
                        </div>
                    )}
                </div>

      {/* System Status */}
<div
    className="
        rounded-2xl p-8 
        shadow-2xl 
        bg-gradient-to-br from-[#6a42ff] via-[#7B5CFF] to-[#9d4bff]
        text-white 
        border border-white/10
        backdrop-blur-2xl
    "
>
    {/* Title */}
    <h3 className="text-2xl font-semibold mb-2 tracking-tight">
        System Status
    </h3>
    <p className="text-white/75 mb-8 text-sm">
        All systems operational and synced with Gemini.
    </p>

    {/* Status Cards */}
    <div className="space-y-4">
        {[
            ['Gemini 2.0 Flash', 'Online'],
            ['Vector DB', 'Connected'],
            ['RAG Engine', 'Active'],
        ].map(([label, status], idx) => (
            <div
                key={idx}
                className="
                    flex items-center justify-between
                    p-4 
                    rounded-xl
                    bg-white/10 
                    border border-white/20
                    backdrop-blur-xl 
                    shadow-lg
                    hover:bg-white/20 hover:border-purple-300
                    transition-all
                "
            >
                <div className="flex items-center gap-3">
                    <span className="w-2.5 h-2.5 bg-emerald-400 rounded-full"></span>
                    <span className="text-white/90">{label}</span>
                </div>
                <span className="text-sm text-white/70">{status}</span>
            </div>
        ))}
    </div>

    {/* QUICK STATS */}
    <div
        className="
            mt-8 
            p-5 
            rounded-xl
            bg-white/10 
            backdrop-blur-xl 
            border border-white/20
            shadow-xl
        "
    >
        <p className="text-sm text-white/80 mb-4">Quick Stats</p>

        <div className="grid grid-cols-2 gap-6">

            {/* Articles Indexed */}
            <div>
                <p className="text-4xl font-semibold text-white drop-shadow-md">
                    {metrics.find(m => m.title === 'Total Articles')?.value || '0'}
                </p>
                <p className="text-xs text-white/60 mt-1">Articles Indexed</p>
            </div>

            {/* Queries Processed */}
            <div>
                <p className="text-4xl font-semibold text-white drop-shadow-md">
                    {metrics.find(m => m.title === 'Total Queries')?.value || '0'}
                </p>
                <p className="text-xs text-white/60 mt-1">Queries Processed</p>
            </div>

        </div>
    </div>
</div>


            </div>

        </div>
    );
};

export default Dashboard;
