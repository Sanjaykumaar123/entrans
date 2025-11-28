import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Sidebar from './components/Sidebar';   // now header (horizontal)
import Dashboard from './pages/Dashboard';
import Chat from './pages/Chat';
import Benchmark from './pages/Benchmark';
import Reports from './pages/Reports';
import Settings from './pages/Settings';

function App() {
    return (
        <Router>

            {/* TOP HEADER */}
            <Sidebar />

            {/* MAIN CONTENT */}
            <main
                className="
                    pt-24 
                    min-h-screen 
                    bg-gradient-to-b from-[#050816] via-[#0e0a2a] to-[#050816]
                    text-white
                "
            >
                <Routes>
                    <Route path="/" element={<Dashboard />} />
                    <Route path="/chat" element={<Chat />} />
                    <Route path="/benchmark" element={<Benchmark />} />
                    <Route path="/reports" element={<Reports />} />
                    <Route path="/settings" element={<Settings />} />
                </Routes>
            </main>

        </Router>
    );
}

export default App;
