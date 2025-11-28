// src/components/RAGResults.jsx
import React from 'react';
import { FileText, ExternalLink } from 'lucide-react';

const RAGResults = ({ data }) => {
    return (
        <div className="w-full max-w-2xl rounded-2xl overflow-hidden bg-slate-950/95 border border-slate-800 shadow-xl">
            {/* Header */}
            <div className="bg-gradient-to-r from-primary via-fuchsia-500 to-sky-500 px-4 py-3 flex items-center justify-between">
                <div className="flex items-center gap-2 text-white text-sm font-medium">
                    <span className="inline-flex h-7 w-7 items-center justify-center rounded-xl bg-black/20">
                        <FileText size={16} />
                    </span>
                    <span>RAG Retrieval Answer</span>
                </div>
                <span className="text-[11px] bg-black/25 text-white/90 px-2 py-1 rounded-full">
                    {data.sources?.length || 0} sources used
                </span>
            </div>

            {/* Body */}
            <div className="px-4 py-4 md:px-5 md:py-5 space-y-4">
                {/* Final answer */}
                <div>
                    <h4 className="text-xs tracking-wide text-slate-400 uppercase mb-1.5">
                        Generated Answer
                    </h4>
                    <p className="text-sm md:text-[15px] leading-relaxed text-slate-50">
                        {data.final_answer}
                    </p>
                </div>

                {/* Sources */}
                {data.sources && data.sources.length > 0 && (
                    <div>
                        <h4 className="text-xs tracking-wide text-slate-400 uppercase mb-2">
                            Sources
                        </h4>
                        <div className="space-y-2">
                            {data.sources.map((source, idx) => (
                                <button
                                    key={idx}
                                    type="button"
                                    className="w-full flex items-center justify-between gap-2 px-3 py-2 rounded-xl bg-slate-900/80 hover:bg-slate-800 transition-colors text-left group"
                                >
                                    <span className="text-xs md:text-sm text-slate-200 truncate group-hover:text-white">
                                        {source}
                                    </span>
                                    <ExternalLink
                                        size={14}
                                        className="text-slate-500 group-hover:text-slate-200 shrink-0"
                                    />
                                </button>
                            ))}
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default RAGResults;
