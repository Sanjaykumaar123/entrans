import React, { useEffect, useState } from 'react';
import { api } from '../api/client';
import { BarChart3, Activity, Zap } from 'lucide-react';

const Benchmark = () => {
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState(null);

    useEffect(() => {
        runBenchmark();
    }, []);

    const runBenchmark = async () => {
        setLoading(true);
        try {
            const response = await api.benchmark();
            if (response.data.status === 'success') {
                const metricsBlock = response.data.ui_blocks.find(b => b.type === 'metrics');
                if (metricsBlock) {
                    setResults(metricsBlock.items);
                }
            }
        } catch (error) {
            console.error("Benchmark failed:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen p-8 bg-gradient-to-b from-[#050816] via-[#0e0a2a] to-[#050816] text-white">
            
            {/* Page Header */}
            <div className="max-w-6xl mx-auto mb-10">
                <h1 className="text-4xl font-semibold tracking-tight">Model Benchmark</h1>
                <p className="text-white/60 mt-1 text-sm">
                    Compare performance of Traditional, NLU, and RAG-Enhanced LLM models.
                </p>
            </div>

            {/* Benchmark Card */}
            <div className="max-w-6xl mx-auto bg-white/90 glass-card backdrop-blur-xl rounded-2xl shadow-xl p-8 border border-white/10">

                {/* Header */}
                <div className="flex items-center justify-between mb-8">
                    <div>
                        <h3 className="text-2xl font-semibold text-gray-900">Performance Metrics</h3>
                        <p className="text-gray-600 text-sm">
                            Automated accuracy / F1 / latency comparison
                        </p>
                    </div>

                    <button
                        onClick={runBenchmark}
                        disabled={loading}
                        className="px-6 py-3 bg-primary text-white rounded-xl hover:bg-primary/90 
                                   transition-all disabled:opacity-50 flex items-center gap-2 shadow-lg shadow-primary/30"
                    >
                        {loading ? <Activity className="animate-spin" size={20} /> : <Zap size={20} />}
                        <span>{loading ? 'Running...' : 'Run Benchmark'}</span>
                    </button>
                </div>

                {/* Results Grid */}
                {results ? (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                        {results.map((metric, idx) => (
                            <div
                                key={idx}
                                className="p-6 bg-gray-50 rounded-2xl border border-gray-200 
                                           hover:border-primary/40 transition-all shadow-sm"
                            >
                                <p className="text-gray-500 text-sm mb-1">{metric.label}</p>
                                <h4 className="text-3xl font-semibold text-gray-900">{metric.value}</h4>
                                <span className="text-xs text-emerald-600 font-medium">
                                    {metric.change}
                                </span>
                            </div>
                        ))}
                    </div>
                ) : (
                    <div className="text-center py-12 bg-gray-100 rounded-xl border border-gray-200">
                        <BarChart3 className="mx-auto text-gray-400 mb-3" size={48} />
                        <p className="text-gray-600">Click "Run Benchmark" to start evaluation</p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Benchmark;
