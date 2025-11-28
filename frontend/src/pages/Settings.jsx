import React, { useState, useEffect } from 'react';
import { Save, Key, Shield, AlertTriangle } from 'lucide-react';
import { api } from '../api/client';

const Settings = () => {
    const [apiKey, setApiKey] = useState('');
    const [saved, setSaved] = useState(false);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const load = async () => {
            try {
                const res = await api.getSettings();
                if (res.data.has_api_key) {
                    setApiKey("********************");
                    setSaved(true);
                }
            } catch {}
        };
        load();
    }, []);

    const saveKey = async () => {
        setLoading(true);
        try {
            await api.saveSettings({ google_api_key: apiKey });
            setSaved(true);
            alert("API key saved! System will restart.");
        } catch {
            alert("Saving failed.");
        }
        setLoading(false);
    };

    return (
        <div className="min-h-screen p-8 bg-gradient-to-b from-[#050816] via-[#0e0a2a] to-[#050816] text-white">

            <div className="max-w-3xl mx-auto mb-10">
                <h1 className="text-4xl font-semibold tracking-tight">Settings</h1>
                <p className="text-white/60 mt-1 text-sm">Configure your AI Agent and API Keys.</p>
            </div>

            {/* API Key Card */}
            <div className="max-w-3xl mx-auto glass-card bg-white/90 border border-white/10 rounded-2xl p-8 shadow-xl mb-10">
                <div className="flex items-center gap-4 mb-6">
                    <div className="w-14 h-14 bg-primary/10 rounded-full flex items-center justify-center text-primary">
                        <Key size={26} />
                    </div>
                    <div>
                        <h3 className="text-xl font-semibold text-gray-900">Gemini API Key</h3>
                        <p className="text-gray-600 text-sm">Required for smart LLM-powered responses.</p>
                    </div>
                </div>

                <div className="bg-blue-50 border border-blue-100 text-blue-800 p-4 rounded-xl flex gap-3 mb-6">
                    <Shield size={20} className="mt-1" />
                    <p className="text-sm">
                        Your API key is securely stored locally.  
                        <a className="underline ml-1" href="https://aistudio.google.com/app/apikey" target="_blank">
                            Click here to get one
                        </a>
                    </p>
                </div>

                <div className="flex gap-4">
                    <input
                        type="password"
                        value={apiKey}
                        onChange={(e) => { setApiKey(e.target.value); setSaved(false); }}
                        placeholder="AIzaSy..."
                        className="flex-1 p-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-primary/20 outline-none"
                    />

                    <button
                        onClick={saveKey}
                        disabled={loading}
                        className={`px-6 py-3 rounded-xl text-white flex items-center gap-2 shadow-md transition-all 
                            ${saved ? 'bg-green-600' : 'bg-primary hover:bg-primary/90'}`}
                    >
                        <Save size={18} />
                        {saved ? 'Saved' : loading ? 'Saving...' : 'Save Key'}
                    </button>
                </div>
            </div>

            {/* Coming Soon */}
            <div className="max-w-3xl mx-auto glass-card bg-white/70 border border-white/20 rounded-2xl p-8 shadow-xl">
                <div className="flex items-center gap-4 mb-4">
                    <div className="w-12 h-12 bg-gray-100 rounded-full flex items-center justify-center text-gray-500">
                        <AlertTriangle size={22} />
                    </div>
                    <div>
                        <h3 className="text-xl font-semibold text-gray-900">Advanced Configuration</h3>
                        <p className="text-gray-600 text-sm">Coming soon: RAG tuning + Model selection.</p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Settings;
