// src/components/ChatWindow.jsx
import React, { useState, useRef, useEffect } from 'react';
import { Send, Bot, User, Sparkles } from 'lucide-react';
import { api } from '../api/client';
import RAGResults from './RAGResults';

const ChatWindow = () => {
    const [messages, setMessages] = useState([
        {
            type: 'chat_reply',
            message:
                'Hi! I’m your AI News Intelligence Agent. Ask me to summarise news, run a RAG search, or classify text.',
            sender: 'ai',
        },
    ]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);
    const messagesEndRef = useRef(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(scrollToBottom, [messages, loading]);

    const handleSend = async () => {
        if (!input.trim()) return;

        const userMsg = { type: 'chat_reply', message: input, sender: 'user' };
        setMessages((prev) => [...prev, userMsg]);
        const query = input;
        setInput('');
        setLoading(true);

        try {
            let response;
            const lower = query.toLowerCase();

            // Simple intent routing – same logic, just formatted
            if (lower.includes('classify')) {
                response = await api.classify(query);
            } else if (lower.includes('news') || lower.includes('search') || lower.includes('rag')) {
                response = await api.ragSearch(query);
            } else {
                // Default to RAG for generic queries
                response = await api.ragSearch(query);
            }

            if (response.data.status === 'success' || response.data.status === 'error') {
                const newBlocks = response.data.ui_blocks.map((block) => ({
                    ...block,
                    sender: 'ai',
                }));
                setMessages((prev) => [...prev, ...newBlocks]);
            }
        } catch (error) {
            console.error(error);
            setMessages((prev) => [
                ...prev,
                {
                    type: 'chat_reply',
                    message: 'Error: Could not connect to the AI agent. Please try again.',
                    sender: 'ai',
                },
            ]);
        } finally {
            setLoading(false);
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    };

    return (
        <div className="flex flex-col h-full gap-4">
            {/* Main chat card */}
            <div className="flex-1 overflow-hidden">
                <div className="h-full glass-card rounded-3xl px-3 py-3 md:px-6 md:py-5 bg-white/85 backdrop-blur-xl border border-white/60 shadow-2xl shadow-black/20 flex flex-col">
                    {/* Small status bar */}
                    <div className="flex items-center justify-between mb-3 md:mb-4">
                        <div className="flex items-center gap-2 text-xs md:text-sm text-slate-600">
                            <span className="inline-flex h-6 w-6 items-center justify-center rounded-full bg-primary/10 text-primary">
                                <Bot size={14} />
                            </span>
                            <span className="font-medium">RAG + Classification Engine</span>
                        </div>
                        <div className="hidden md:flex items-center gap-2 text-[11px] text-slate-400">
                            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                            <span>Connected</span>
                        </div>
                    </div>

                    {/* Messages */}
                    <div className="flex-1 overflow-y-auto space-y-4 md:space-y-5 pr-1 custom-scroll">
                        {messages.map((msg, idx) => (
                            <div
                                key={idx}
                                className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}
                            >
                                <div
                                    className={`flex max-w-3xl ${
                                        msg.sender === 'user' ? 'flex-row-reverse' : 'flex-row'
                                    } items-start gap-3 md:gap-4`}
                                >
                                    {/* Avatar */}
                                    <div
                                        className={`w-8 h-8 md:w-9 md:h-9 rounded-full flex items-center justify-center shrink-0 shadow-md ${
                                            msg.sender === 'user'
                                                ? 'bg-gradient-to-br from-[#FF50C8] to-[#7B5CFF]'
                                                : 'bg-primary'
                                        }`}
                                    >
                                        {msg.sender === 'user' ? (
                                            <User size={16} className="text-white" />
                                        ) : (
                                            <Bot size={16} className="text-white" />
                                        )}
                                    </div>

                                    <div
                                        className={`space-y-2 flex flex-col ${
                                            msg.sender === 'user' ? 'items-end' : 'items-start'
                                        }`}
                                    >
                                        {/* Simple text reply */}
                                        {msg.type === 'chat_reply' && (
                                            <div
                                                className={`px-4 py-3 md:px-5 md:py-3 rounded-2xl text-sm md:text-[15px] leading-relaxed shadow-sm ${
                                                    msg.sender === 'user'
                                                        ? 'bg-white text-slate-900 border border-slate-100 rounded-tr-sm'
                                                        : 'bg-slate-900 text-slate-50 rounded-tl-sm'
                                                }`}
                                            >
                                                <p className="whitespace-pre-line">{msg.message}</p>
                                            </div>
                                        )}

                                        {/* Generic card block (debug / metrics) */}
                                        {msg.type === 'card' && (
                                            <div className="bg-white px-4 py-3 rounded-2xl shadow-md border border-slate-100 w-full">
                                                <h3 className="font-semibold text-primary mb-2 text-sm">
                                                    {msg.title}
                                                </h3>
                                                <pre className="text-xs bg-slate-50 px-3 py-2 rounded-lg overflow-x-auto">
                                                    {JSON.stringify(msg.content, null, 2)}
                                                </pre>
                                            </div>
                                        )}

                                        {/* RAG result block */}
                                        {msg.type === 'rag_result' && <RAGResults data={msg} />}
                                    </div>
                                </div>
                            </div>
                        ))}

                        {/* Typing indicator */}
                        {loading && (
                            <div className="flex justify-start">
                                <div className="bg-slate-900 text-white px-4 py-3 rounded-2xl rounded-tl-sm shadow-md flex items-center gap-2 text-xs">
                                    <span className="w-2 h-2 bg-emerald-400 rounded-full animate-bounce" />
                                    <span className="w-2 h-2 bg-emerald-400 rounded-full animate-bounce delay-75" />
                                    <span className="w-2 h-2 bg-emerald-400 rounded-full animate-bounce delay-150" />
                                    <span className="ml-1 text-[11px] text-white/70 hidden md:inline">
                                        Thinking with RAG…
                                    </span>
                                </div>
                            </div>
                        )}

                        <div ref={messagesEndRef} />
                    </div>
                </div>
            </div>

            {/* Input area */}
            <div className="pb-1">
                <div className="glass-card rounded-2xl px-3 py-2 md:px-5 md:py-3 bg-white/90 backdrop-blur-xl border border-white/60 shadow-xl">
                    <div className="flex items-center gap-3 md:gap-4">
                        <div className="hidden md:flex items-center gap-1 text-xs text-slate-500">
                            <Sparkles size={14} className="text-primary" />
                            <span>Press Enter to send • Shift+Enter for new line</span>
                        </div>

                        <input
                            type="text"
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            onKeyDown={handleKeyDown}
                            placeholder="Ask about news, run a RAG search, or say 'classify:' followed by text…"
                            className="flex-1 bg-transparent border-none outline-none text-sm md:text-[15px] placeholder:text-slate-400"
                        />

                        <button
                            onClick={handleSend}
                            disabled={loading}
                            className="inline-flex items-center justify-center rounded-xl px-3 py-2 md:px-4 md:py-2 bg-primary text-white text-sm font-medium shadow-lg shadow-primary/40 disabled:opacity-60 disabled:cursor-not-allowed hover:bg-primary/90 transition-all"
                        >
                            <Send size={18} className="mr-1 hidden md:inline" />
                            <span>{loading ? 'Sending…' : 'Send'}</span>
                        </button>
                    </div>

                    {/* Quick suggestions */}
                    <div className="mt-2 flex flex-wrap gap-2 text-[11px] text-slate-500">
                        <button
                            type="button"
                            className="px-2.5 py-1 rounded-full bg-slate-100 hover:bg-slate-200 transition-colors"
                            onClick={() => setInput('Summarise today’s top AI news.')}
                        >
                            Summarise today’s AI news
                        </button>
                        <button
                            type="button"
                            className="px-2.5 py-1 rounded-full bg-slate-100 hover:bg-slate-200 transition-colors"
                            onClick={() =>
                                setInput('Classify this article as trustworthy or misleading: ')
                            }
                        >
                            Classify an article
                        </button>
                        <button
                            type="button"
                            className="px-2.5 py-1 rounded-full bg-slate-100 hover:bg-slate-200 transition-colors"
                            onClick={() => setInput('Search news about climate policy with RAG.')}
                        >
                            RAG search on a topic
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ChatWindow;
