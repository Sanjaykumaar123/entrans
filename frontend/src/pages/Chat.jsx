// src/pages/Chat.jsx
import React from 'react';
import { Bot } from 'lucide-react';
import ChatWindow from '../components/ChatWindow';

const Chat = () => {
    return (
        <div className="h-screen flex flex-col bg-gradient-to-b from-[#050816] via-[#120c3b] to-[#050816]">
            
            {/* Top compact header */}
            <div className="px-6 md:px-10 pt-8 pb-4 border-b border-white/10">
                <div className="max-w-5xl mx-auto">
                    
                    {/* Small badge */}
                    <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full 
                        bg-white/10 text-[11px] md:text-xs text-white/80 mb-3">
                        <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                        <span>RAG + Classification Engine</span>
                    </div>

                    {/* Page Title Only */}
                    <h1 className="text-3xl md:text-4xl font-semibold text-white flex items-center gap-3">
                        <span className="inline-flex h-11 w-11 items-center justify-center rounded-2xl 
                            bg-white/10 shadow-lg shadow-black/30">
                            <Bot size={22} />
                        </span>
                        AI Chat Agent
                    </h1>
                </div>
            </div>

            {/* Chat Window */}
            <div className="flex-1">
                <div className="h-full max-w-5xl mx-auto px-3 md:px-6 py-4 md:py-6">
                    <ChatWindow />
                </div>
            </div>
        </div>
    );
};

export default Chat;
