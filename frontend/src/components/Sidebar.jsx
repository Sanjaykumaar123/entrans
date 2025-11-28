import React from "react";
import { Link, useLocation } from "react-router-dom";
import {
    LayoutDashboard,
    MessageSquare,
    FileText,
    Activity,
    Settings
} from "lucide-react";

const Sidebar = () => {
    const location = useLocation();

    const navItems = [
        { label: "Dashboard", icon: LayoutDashboard, path: "/" },
        { label: "Chat Agent", icon: MessageSquare, path: "/chat" },
        { label: "Benchmark", icon: Activity, path: "/benchmark" },
        { label: "Reports", icon: FileText, path: "/reports" },
    ];

    return (
        <header
            className="
                fixed top-0 left-0 w-full z-50 
        bg-gradient-to-r from-[#0a071d] via-[#120c3b] to-[#050816]
        backdrop-blur-xl
        shadow-[0_4px_25px_rgba(0,0,0,0.5)]
        border-b border-transparent
            "
        >
            <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">

                {/* LOGO */}
                <Link to="/" className="flex items-center gap-2">
                    <h1 className="text-2xl font-bold tracking-wide text-white">
                        <span className="bg-gradient-to-r from-[#7B5CFF] to-[#FF50C8] bg-clip-text text-transparent">
                            THINK
                        </span>{" "}
                        BOT
                    </h1>
                </Link>

                {/* NAVIGATION */}
                <nav className="flex items-center gap-6">
                    {navItems.map(({ label, icon: Icon, path }) => {
                        const isActive = location.pathname === path;

                        return (
                            <Link
                                key={path}
                                to={path}
                                className={`
                                    flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium transition-all
                                    ${
                                        isActive
                                            ? "bg-white/10 text-white border border-white/20 shadow-lg shadow-primary/30"
                                            : "text-white/60 hover:text-white hover:bg-white/5"
                                    }
                                `}
                            >
                                <Icon size={18} className={isActive ? "text-primary" : "text-white/70"} />
                                {label}
                            </Link>
                        );
                    })}
                </nav>

                {/* SETTINGS BUTTON */}
                <Link
                    to="/settings"
                    className="
                        flex items-center gap-2 px-4 py-2 text-white/60 hover:text-white
                        bg-white/5 hover:bg-white/10 rounded-xl transition-all
                    "
                >
                    <Settings size={18} />
                    <span className="hidden md:block">Settings</span>
                </Link>
            </div>
        </header>
    );
};

export default Sidebar;
