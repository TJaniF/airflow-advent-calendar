import React, { useState, useEffect } from 'react';

const CalendarWindow = ({ day, isOpen, text }) => {
  const style = {
    width: '100px',
    height: '100px',
    backgroundColor: isOpen ? '#2ecc71' : '#e74c3c', 
    color: 'white',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    margin: '10px',
    borderRadius: '8px',
    cursor: isOpen ? 'pointer' : 'not-allowed',
    opacity: isOpen ? 1 : 0.6,
    transition: 'transform 0.2s',
    fontSize: '1.2rem',
    fontWeight: 'bold',
    boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
    flexDirection: 'column'
  };

  const handleClick = () => {
    if (isOpen) {
      alert(`Opening window for Day ${day}! \n(Link will go here)`);
    } else {
      alert(`Day ${day} is not open yet! Run DAG 'day_${day}' to unlock.`);
    }
  };

  return (
    <div 
      style={style} 
      onClick={handleClick}
      onMouseEnter={(e) => { if(isOpen) e.currentTarget.style.transform = 'scale(1.05)'; }}
      onMouseLeave={(e) => { if(isOpen) e.currentTarget.style.transform = 'scale(1)'; }}
    >
      <div>{day}</div>
      {isOpen && <div style={{fontSize: '0.8rem', marginTop: '5px'}}>Open!</div>}
    </div>
  );
};

const AdventCalendarWidget = () => {
  const [days, setDays] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const response = await fetch('/advent-calendar-plugin/calendar-status');
        if (!response.ok) {
          throw new Error('Failed to fetch calendar status');
        }
        const data = await response.json();
        setDays(data);
      } catch (err) {
        console.error("Error fetching calendar status:", err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchStatus();
  }, []);

  if (loading) return <div style={{ padding: '20px' }}>Loading Calendar... 🎄</div>;
  if (error) return <div style={{ padding: '20px', color: 'red' }}>Error: {error}</div>;

  return (
    <div style={{ padding: '20px' }}>
      <h1 style={{ textAlign: 'center', marginBottom: '20px' }}>🎄 Airflow Advent Calendar 🎄</h1>
      <div style={{ 
        display: 'flex', 
        flexWrap: 'wrap', 
        justifyContent: 'center',
        maxWidth: '800px',
        margin: '0 auto'
      }}>
        {Object.values(days).map((dayData) => (
          <CalendarWindow 
            key={dayData.day} 
            day={dayData.day} 
            isOpen={dayData.isOpen} 
            text={dayData.text} 
          />
        ))}
      </div>
    </div>
  );
};

export default AdventCalendarWidget;

