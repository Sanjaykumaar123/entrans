import React from 'react';
import { TrendingUp, TrendingDown, Minus } from 'lucide-react';

const MetricsCard = ({ title, value, change, icon: Icon }) => {
    const isPositive = change?.startsWith('+');
    const isNeutral = change === 'N/A' || !change;

    return (
        <div
            className="
                glass-card bg-white/90 
                border border-white/20 
                p-6 rounded-2xl shadow-xl 
                hover:shadow-primary/20 
                transition-all 
                backdrop-blur-xl
            "
        >
            <div className="flex justify-between items-start mb-2">
                <div>
                    <p className="text-sm font-medium text-gray-600">{title}</p>
                    <h3 className="text-3xl font-semibold text-gray-900 mt-1">{value}</h3>
                </div>

                <div
                    className="
                        p-3 rounded-xl 
                        bg-primary/10 
                        text-primary 
                        shadow-md 
                        shadow-primary/20
                    "
                >
                    {Icon && <Icon size={24} />}
                </div>
            </div>

            {/* Change Indicator */}
            <div className="mt-4 flex items-center space-x-2">
                {isNeutral ? (
                    <span className="flex items-center text-gray-400 text-sm font-medium">
                        <Minus size={16} className="mr-1" />
                        Stable
                    </span>
                ) : (
                    <span
                        className={`flex items-center text-sm font-medium ${
                            isPositive ? 'text-emerald-500' : 'text-red-500'
                        }`}
                    >
                        {isPositive ? (
                            <TrendingUp size={16} className="mr-1" />
                        ) : (
                            <TrendingDown size={16} className="mr-1" />
                        )}
                        {change}
                    </span>
                )}

                <span className="text-xs text-gray-400">vs last run</span>
            </div>
        </div>
    );
};

export default MetricsCard;
