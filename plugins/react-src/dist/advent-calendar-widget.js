(function() {
  
  var React = window.React;
  if (!React) {
    console.error("React not found on window. The Advent Calendar Plugin cannot render.");
    return;
  }

  var e = React.createElement;
  var useState = React.useState;
  var useEffect = React.useEffect;

  var snowflakeStyle = document.createElement('style');
  snowflakeStyle.innerHTML = `
    @keyframes snowfall {
      0% { transform: translateY(-10px) rotate(0deg); opacity: 1; }
      100% { transform: translateY(100vh) rotate(360deg); opacity: 0.3; }
    }
    .snowflake {
      position: fixed;
      top: -10px;
      z-index: 9999;
      color: #FFF;
      font-size: 1em;
      user-select: none;
      pointer-events: none;
      animation-name: snowfall;
      animation-timing-function: linear;
      animation-iteration-count: infinite;
    }
    @keyframes twinkle {
      0% { opacity: 0.5; transform: scale(0.8); }
      100% { opacity: 1; transform: scale(1.2); }
    }
    @keyframes santaSled {
      0% { 
        left: -200px; 
        top: 20%;
        opacity: 0;
      }
      1% {
        opacity: 1;
      }
      10% {
        opacity: 1;
      }
      11% { 
        left: calc(100% + 200px); 
        top: 30%;
        opacity: 0;
      }
      100% {
        left: calc(100% + 200px);
        top: 30%;
        opacity: 0;
      }
    }
    @keyframes rudolphEasterEgg {
      0%, 99% {
        opacity: 0;
        visibility: hidden;
      }
      100% {
        opacity: 1;
        visibility: visible;
      }
    }
    @keyframes rudolphNotification {
      0% {
        transform: translateX(-600px);
        opacity: 1;
      }
      95% {
        opacity: 1;
      }
      100% {
        transform: translateX(calc(100vw + 600px));
        opacity: 0;
      }
    }
  `;
  document.head.appendChild(snowflakeStyle);

  var colors = {
    bg: '#1a1a2e',
    gold: '#D4AF37',
    text: '#3e2723',
    theme: [
      '#842113',
      '#007880',
      '#00943C',
      '#002C55'
    ]
  };

  var styles = {
    container: {
      fontFamily: "'Inter', 'Segoe UI', 'Roboto', sans-serif",
      background: 'linear-gradient(to bottom, #1a1a2e 0%, #16213e 40%, #eef2f3 100%)',
      height: '100vh',
      width: '100vw',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      color: colors.text,
      position: 'fixed',
      top: 0,
      left: 0,
      overflow: 'hidden'
    },
    header: {
      backgroundColor: 'transparent',
      color: '#F3E5AB',
      width: '100%',
      textAlign: 'center',
      padding: '20px 0 10px',
      fontSize: '3rem',
      fontWeight: '800',
      letterSpacing: '-1px',
      textTransform: 'uppercase',
      marginBottom: '10px',
      borderBottom: 'none',
      boxShadow: 'none',
      zIndex: 10,
      textShadow: '0 0 10px rgba(243, 229, 171, 0.6)'
    },
    treeContainer: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: '10px',
      position: 'relative',
      zIndex: 10,
      marginTop: '0px',
      paddingBottom: '20px'
    },
    row: {
      display: 'flex',
      justifyContent: 'center',
      gap: '15px'
    },
    scene: {
      position: 'absolute',
      bottom: 0,
      left: 0,
      width: '100%',
      height: '100%',
      zIndex: 0,
      pointerEvents: 'none'
    },
    ground: {
      position: 'absolute',
      bottom: 0,
      left: 0,
      width: '100%',
      height: '30vh',
      background: 'linear-gradient(to top, #e6e9f0 0%, #eef1f5 100%)',
      borderRadius: '100% 100% 0 0 / 20% 20% 0 0',
      transform: 'scaleX(1.5)',
      zIndex: 1
    },
    mountain1: {
      position: 'absolute',
      bottom: '20vh',
      left: '10%',
      width: '0',
      height: '0',
      borderLeft: '200px solid transparent',
      borderRight: '200px solid transparent',
      borderBottom: '300px solid #dbe4eb',
      zIndex: 0
    },
    mountain2: {
      position: 'absolute',
      bottom: '20vh',
      right: '15%',
      width: '0',
      height: '0',
      borderLeft: '250px solid transparent',
      borderRight: '250px solid transparent',
      borderBottom: '400px solid #c4d3df',
      zIndex: 0
    },
    smallTree: {
      width: '0', height: '0',
      borderLeft: '15px solid transparent',
      borderRight: '15px solid transparent',
      borderBottom: '40px solid #2f5233',
      position: 'absolute',
      zIndex: 1,
      filter: 'drop-shadow(0 5px 5px rgba(0,0,0,0.1))'
    },
    smallTreeLayer: {
        position: 'absolute',
        top: '15px',
        left: '-20px',
        width: '0', height: '0',
        borderLeft: '20px solid transparent',
        borderRight: '20px solid transparent',
        borderBottom: '30px solid #2f5233',
    },
    star: {
      position: 'absolute',
      backgroundColor: '#fff',
      borderRadius: '50%',
      opacity: 0.8,
      animation: 'twinkle 2s infinite alternate'
    },
    moon: {
      position: 'absolute',
      top: '10%',
      right: '10%',
      width: '100px',
      height: '100px',
      borderRadius: '50%',
      backgroundColor: '#f4e8c1',
      boxShadow: '0 0 40px rgba(244, 232, 193, 0.6), inset -10px -10px 20px rgba(0,0,0,0.1)',
      zIndex: 5
    },
    treeLight: {
      position: 'absolute',
      width: '8px',
      height: '8px',
      borderRadius: '50%',
      zIndex: 4,
      boxShadow: '0 0 10px currentColor',
      animation: 'twinkle 1.5s infinite alternate'
    },
    santaSled: {
      position: 'fixed',
      left: '-200px',
      top: '20%',
      zIndex: 9998,
      filter: 'drop-shadow(0 2px 4px rgba(0,0,0,0.3))',
      pointerEvents: 'none',
      display: 'flex',
      alignItems: 'center',
      gap: '5px',
      opacity: 0,
      visibility: 'hidden',
      animation: 'rudolphEasterEgg 120s steps(1, end) 1 forwards, santaSled 135s linear 120s infinite'
    },
    reindeer: {
      width: '30px',
      height: '25px',
      position: 'relative'
    },
    reindeerBody: {
      width: '20px',
      height: '12px',
      backgroundColor: '#8B4513',
      borderRadius: '8px',
      position: 'absolute',
      bottom: '0',
      left: '5px'
    },
    reindeerHead: {
      width: '12px',
      height: '10px',
      backgroundColor: '#8B4513',
      borderRadius: '6px',
      position: 'absolute',
      top: '0',
      right: '0'
    },
    reindeerAntler: {
      width: '2px',
      height: '6px',
      backgroundColor: '#654321',
      position: 'absolute',
      top: '-4px'
    },
    reindeerNose: {
      width: '4px',
      height: '4px',
      backgroundColor: '#ff0000',
      borderRadius: '50%',
      position: 'absolute',
      right: '-2px',
      top: '4px'
    },
    reindeerLeg: {
      width: '2px',
      height: '8px',
      backgroundColor: '#654321',
      position: 'absolute',
      bottom: '-8px'
    },
    sled: {
      width: '50px',
      height: '30px',
      position: 'relative',
      marginLeft: '10px'
    },
    sledBase: {
      width: '40px',
      height: '15px',
      backgroundColor: '#8B0000',
      borderRadius: '0 0 20px 20px',
      position: 'absolute',
      bottom: '8px',
      left: '5px'
    },
    sledRunner: {
      width: '45px',
      height: '4px',
      backgroundColor: '#FFD700',
      borderRadius: '20px',
      position: 'absolute',
      bottom: '2px',
      left: '2px'
    },
    santa: {
      width: '18px',
      height: '22px',
      backgroundColor: '#ff0000',
      borderRadius: '8px',
      position: 'absolute',
      top: '2px',
      left: '15px'
    },
    santaHead: {
      width: '12px',
      height: '12px',
      backgroundColor: '#ffd1a3',
      borderRadius: '50%',
      position: 'absolute',
      top: '-8px',
      left: '3px'
    },
    santaHat: {
      width: '0',
      height: '0',
      borderLeft: '8px solid transparent',
      borderRight: '8px solid transparent',
      borderBottom: '10px solid #ff0000',
      position: 'absolute',
      top: '-14px',
      left: '-2px'
    },
    treeBackground: {
      position: 'absolute',
      top: '30px',
      left: '50%',
      transform: 'translateX(-50%)',
      zIndex: 0,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    },
    treeLayer1: {
      width: '0', height: '0',
      borderLeft: '150px solid transparent',
      borderRight: '150px solid transparent',
      borderBottom: '160px solid #2f5233',
      borderRadius: '20px',
      marginBottom: '-70px',
      zIndex: 3
    },
    treeLayer2: {
      width: '0', height: '0',
      borderLeft: '220px solid transparent',
      borderRight: '220px solid transparent',
      borderBottom: '230px solid #26472b',
      borderRadius: '30px',
      marginBottom: '-90px',
      zIndex: 2
    },
    treeLayer3: {
      width: '0', height: '0',
      borderLeft: '300px solid transparent',
      borderRight: '300px solid transparent',
      borderBottom: '310px solid #1e3c24',
      borderRadius: '40px',
      zIndex: 1
    },
    treeTrunk: {
      width: '60px',
      height: '80px',
      backgroundColor: '#3e2723',
      borderRadius: '0 0 10px 10px',
      marginTop: '-10px',
      zIndex: 0,
      boxShadow: 'inset -3px -3px 8px rgba(0,0,0,0.3)'
    },
    window: {
      position: 'relative',
      width: '80px',
      height: '80px',
      borderRadius: '50%',
      cursor: 'pointer',
      transition: 'transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      overflow: 'visible',
      border: '2px solid rgba(255, 255, 255, 0.3)',
      boxShadow: 'inset -8px -8px 20px rgba(0,0,0,0.15), inset 8px 8px 20px rgba(255,255,255,0.4), 0 8px 20px rgba(0,0,0,0.2), 0 2px 5px rgba(0,0,0,0.1)',
      backgroundColor: '#fff',
      zIndex: 5,
      backdropFilter: 'blur(10px)'
    },
    number: {
      fontSize: '2rem',
      fontWeight: '900',
      zIndex: 2,
      color: '#fff',
      opacity: 0.9,
      fontFamily: "'Georgia', serif",
      lineHeight: '1',
      position: 'relative',
      top: '-2px',
      left: '-1px'
    },
    icon: {
      width: '100%',
      height: '100%',
      objectFit: 'cover',
      borderRadius: '50%',
      zIndex: 1
    },
    closedOverlay: {
      position: 'absolute',
      top: 0,
      left: 0,
      width: '100%',
      height: '100%',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 3,
      flexDirection: 'column'
    }
  };


  var Snowflake = function() {
    var left = Math.random() * 100 + 'vw';
    var duration = (Math.random() * 5 + 5) + 's';
    var delay = (Math.random() * 10 - 10) + 's';
    var size = (Math.random() * 1 + 0.5) + 'rem';
    var opacity = Math.random() * 0.5 + 0.3;

    return e('div', {
      className: 'snowflake',
      style: {
        left: left,
        animationDuration: duration,
        animationDelay: delay,
        fontSize: size,
        opacity: opacity,
        color: '#b0c4de'
      }
    }, '❄');
  };

  var RudolphNotification = function(props) {
    if (!props.show) return null;

    var Reindeer = function(props) {
      var hasRedNose = props.hasRedNose || false;
      return e('div', { style: {
        width: '30px',
        height: '25px',
        position: 'relative'
      }},
        e('div', { style: {
          width: '20px',
          height: '12px',
          backgroundColor: '#8B4513',
          borderRadius: '8px',
          position: 'absolute',
          bottom: '0',
          left: '5px'
        }},
          e('div', { style: {
            width: '3px',
            height: '8px',
            backgroundColor: '#8B4513',
            position: 'absolute',
            bottom: '-6px',
            left: '2px',
            borderRadius: '2px'
          }}),
          e('div', { style: {
            width: '3px',
            height: '8px',
            backgroundColor: '#8B4513',
            position: 'absolute',
            bottom: '-6px',
            left: '8px',
            borderRadius: '2px'
          }}),
          e('div', { style: {
            width: '3px',
            height: '8px',
            backgroundColor: '#8B4513',
            position: 'absolute',
            bottom: '-6px',
            left: '14px',
            borderRadius: '2px'
          }})
        ),
        e('div', { style: {
          width: '12px',
          height: '10px',
          backgroundColor: '#8B4513',
          borderRadius: '6px',
          position: 'absolute',
          top: '0',
          right: '0'
        }},
          e('div', { style: {
            width: '2px',
            height: '6px',
            backgroundColor: '#654321',
            position: 'absolute',
            top: '-4px',
            left: '2px'
          }}),
          e('div', { style: {
            width: '2px',
            height: '6px',
            backgroundColor: '#654321',
            position: 'absolute',
            top: '-4px',
            right: '2px'
          }}),
          hasRedNose ? e('div', { style: {
            width: '4px',
            height: '4px',
            backgroundColor: '#FF0000',
            borderRadius: '50%',
            position: 'absolute',
            top: '3px',
            right: '-2px',
            boxShadow: '0 0 5px #FF0000'
          }}) : null
        )
      );
    };

    return e('div', {
      style: {
        position: 'fixed',
        top: '10%',
        left: '0',
        zIndex: 10000,
        display: 'flex',
        alignItems: 'center',
        gap: '10px',
        animation: 'rudolphNotification 15s linear forwards',
        pointerEvents: 'none',
        filter: 'drop-shadow(2px 2px 5px rgba(0,0,0,0.3))'
      }
    },
      e('div', { style: { 
        position: 'relative',
        backgroundColor: '#f4e4c1',
        background: 'linear-gradient(to bottom, #f4e4c1 0%, #e8d4a8 50%, #f4e4c1 100%)',
        padding: '15px 30px',
        borderRadius: '8px',
        boxShadow: 'inset 0 0 20px rgba(101, 67, 33, 0.2), 0 5px 20px rgba(0,0,0,0.3)',
        border: '2px solid #8B4513',
        borderLeft: '8px solid #654321',
        borderRight: '8px solid #654321',
        fontFamily: "'Georgia', serif",
        fontSize: '1rem',
        fontWeight: 'normal',
        color: '#3e2723',
        maxWidth: '400px',
        textAlign: 'center',
        zIndex: 1
      }}, 'This window is still closed. If it is time to open it, run the corresponding Dag!'),
      e('div', { style: { 
        position: 'relative',
        zIndex: 10,
        transform: 'scale(1)'
      }},
        e(Reindeer, { hasRedNose: true })
      )
    );
  };

  var SmallTree = function(props) {
    var left = props.left;
    var bottom = props.bottom || '25vh';
    var scale = props.scale || 1;
    
    return e('div', { 
      style: Object.assign({}, styles.smallTree, { 
        left: left, 
        bottom: bottom,
        transform: 'scale(' + scale + ')'
      }) 
    },
      e('div', { style: {
        width: '0', height: '0',
        borderLeft: '15px solid transparent',
        borderRight: '15px solid transparent',
        borderBottom: '25px solid #2f5233',
        position: 'absolute', top: '-20px', left: '-15px'
      }}),
      e('div', { style: {
        width: '0', height: '0',
        borderLeft: '20px solid transparent',
        borderRight: '20px solid transparent',
        borderBottom: '30px solid #26472b',
        position: 'absolute', top: '-5px', left: '-20px'
      }})
    );
  };

  var Star = function() {
    var top = Math.random() * 40 + '%';
    var left = Math.random() * 100 + '%';
    var size = Math.random() * 3 + 2 + 'px';
    var delay = Math.random() * 2 + 's';

    return e('div', {
      style: Object.assign({}, styles.star, {
        top: top,
        left: left,
        width: size,
        height: size,
        animationDelay: delay
      })
    });
  };

  var TreeLight = function(props) {
    var color = '#FFD700';
    var top = props.top;
    var left = props.left;
    var delay = Math.random() * 2 + 's';

    return e('div', {
      style: Object.assign({}, styles.treeLight, {
        top: top,
        left: left,
        backgroundColor: color,
        color: color,
        animationDelay: delay
      })
    });
  };

  var SantaSled = function() {
    var Reindeer = function(props) {
      var hasRedNose = props.hasRedNose || false;
      return e('div', { style: styles.reindeer },
        e('div', { style: styles.reindeerBody },
          e('div', { style: Object.assign({}, styles.reindeerLeg, { left: '2px' }) }),
          e('div', { style: Object.assign({}, styles.reindeerLeg, { left: '8px' }) }),
          e('div', { style: Object.assign({}, styles.reindeerLeg, { left: '14px' }) })
        ),
        e('div', { style: styles.reindeerHead },
          e('div', { style: Object.assign({}, styles.reindeerAntler, { left: '2px' }) }),
          e('div', { style: Object.assign({}, styles.reindeerAntler, { right: '2px' }) }),
          hasRedNose ? e('div', { style: styles.reindeerNose }) : null
        )
      );
    };

    return e('div', { style: styles.santaSled },
      e(Reindeer, { hasRedNose: true })
    );
  };

  var CalendarWindow = function(props) {
    var day = props.day;
    var isOpen = props.isOpen;
    var text = props.text;
    var link = props.link;
    var onLockedClick = props.onLockedClick;
    
    var colorIndex = (day * 7) % 4;
    var tileColor = colors.theme[colorIndex];

    var iconUrl = "/advent-calendar-plugin/img/day_" + day + ".png";

    var windowStyle = Object.assign({}, styles.window, {
      backgroundColor: isOpen ? '#ffffff' : tileColor,
      color: isOpen ? colors.text : '#fff',
      background: isOpen 
        ? 'radial-gradient(circle at 25% 25%, rgba(255,255,255,0.9), rgba(255,255,255,0.6) 40%, rgba(230,230,230,0.8))' 
        : 'radial-gradient(circle at 25% 25%, rgba(255,255,255,0.5), rgba(255,255,255,0.2) 40%, transparent 60%), linear-gradient(135deg, ' + tileColor + ' 0%, ' + tileColor + 'dd 100%)',
    });

    var handleClick = function() {
      if (isOpen) {
        if (link) {
          window.open(link, '_blank');
        }
      } else {
        if (onLockedClick) {
          onLockedClick();
        }
      }
    };

    var handleMouseEnter = function(ev) { 
      ev.currentTarget.style.transform = 'scale(1.15) rotate(5deg)'; 
      ev.currentTarget.style.boxShadow = 'inset -10px -10px 25px rgba(0,0,0,0.2), inset 10px 10px 25px rgba(255,255,255,0.5), 0 12px 30px rgba(0,0,0,0.3), 0 0 30px ' + tileColor + '80';
      ev.currentTarget.style.zIndex = '100';
    };
    var handleMouseLeave = function(ev) { 
      ev.currentTarget.style.transform = 'scale(1) rotate(0deg)'; 
      ev.currentTarget.style.boxShadow = 'inset -8px -8px 20px rgba(0,0,0,0.15), inset 8px 8px 20px rgba(255,255,255,0.4), 0 8px 20px rgba(0,0,0,0.2), 0 2px 5px rgba(0,0,0,0.1)';
      ev.currentTarget.style.zIndex = '5';
    };

    var content;
    if (isOpen) {
      content = e('img', { key: 'img', src: iconUrl, style: styles.icon, alt: "Day " + day });
    } else {
      content = e('div', { style: styles.closedOverlay },
        e('span', { style: styles.number }, day)
      );
    }

    return e('div', {
      style: windowStyle,
      onClick: handleClick,
      onMouseEnter: handleMouseEnter,
      onMouseLeave: handleMouseLeave
    }, content);
  };

  var AdventCalendarWidget = function() {
    var state = useState({});
    var days = state[0];
    var setDays = state[1];
    var loadingState = useState(true);
    var loading = loadingState[0];
    var setLoading = loadingState[1];
    var errorState = useState(null);
    var error = errorState[0];
    var setError = errorState[1];
    var notificationState = useState(false);
    var showNotification = notificationState[0];
    var setShowNotification = notificationState[1];

    useEffect(function() {
      fetch('/advent-calendar-plugin/calendar-status')
        .then(function(res) {
          if (!res.ok) throw new Error('Failed to fetch calendar status');
          return res.json();
        })
        .then(function(data) {
          setDays(data);
          setLoading(false);
        })
        .catch(function(err) {
          console.error("Error:", err);
          setError(err.message);
          setLoading(false);
        });
    }, []);

    if (loading) return e('div', { style: { padding: '50px', textAlign: 'center', fontSize: '1.5rem', color: '#FFF' } }, "");
    if (error) return e('div', { style: { padding: '50px', textAlign: 'center', color: 'red' } }, "Error: " + error);

    var seed = 12345; 
    var seededRandom = function() {
      var x = Math.sin(seed++) * 10000;
      return x - Math.floor(x);
    };
    
    var sortedDays = Object.values(days).sort(function(a, b) { return a.day - b.day; });
    
    var day24 = sortedDays.find(function(d) { return d.day === 24; });
    var otherDays = sortedDays.filter(function(d) { return d.day !== 24; });

    for (var i = otherDays.length - 1; i > 0; i--) {
      var j = Math.floor(seededRandom() * (i + 1));
      var temp = otherDays[i];
      otherDays[i] = otherDays[j];
      otherDays[j] = temp;
    }

    var finalOrder = [day24].concat(otherDays);
    
    var index19 = finalOrder.findIndex(function(d) { return d.day === 19; });
    var index3 = finalOrder.findIndex(function(d) { return d.day === 3; });
    if (index19 !== -1 && index3 !== -1) {
      var temp = finalOrder[index19];
      finalOrder[index19] = finalOrder[index3];
      finalOrder[index3] = temp;
    }
    
    var rows = [
      finalOrder.slice(0, 1),
      finalOrder.slice(1, 3),
      finalOrder.slice(3, 6),
      finalOrder.slice(6, 10),
      finalOrder.slice(10, 13),
      finalOrder.slice(13, 18),
      finalOrder.slice(18, 24)
    ];

    var handleLockedClick = function() {
      setShowNotification(true);
      setTimeout(function() {
        setShowNotification(false);
      }, 15000);
    };

    var treeElements = rows.map(function(rowItems, rowIndex) {
      var items = rowItems.map(function(dayData) {
        return e(CalendarWindow, {
          key: dayData.day,
          day: dayData.day,
          isOpen: dayData.isOpen,
          text: dayData.text,
          link: dayData.link,
          onLockedClick: handleLockedClick
        });
      });
      return e('div', { key: rowIndex, style: styles.row }, items);
    });

    var snowflakes = [];
    for (var i = 0; i < 50; i++) {
      snowflakes.push(e(Snowflake, { key: i }));
    }

    var stars = [];
    for (var s = 0; s < 30; s++) {
      stars.push(e(Star, { key: 'star-'+s }));
    }

    var landscapeTrees = [
        e(SmallTree, { key: 't1', left: '8%', bottom: '27vh', scale: 1.3 }),
        e(SmallTree, { key: 't2', left: '15%', bottom: '28vh', scale: 1.2 }),
        e(SmallTree, { key: 't3', left: '22%', bottom: '24vh', scale: 0.9 }),
        e(SmallTree, { key: 't4', left: '72%', bottom: '25vh', scale: 1.0 }),
        e(SmallTree, { key: 't5', left: '78%', bottom: '27vh', scale: 1.2 }),
        e(SmallTree, { key: 't6', left: '85%', bottom: '26vh', scale: 1.1 }),
        e(SmallTree, { key: 't7', left: '92%', bottom: '29vh', scale: 0.8 }),
    ];

    var treeLights = [
      e(TreeLight, { key: 'l1', top: '112px', left: '50.7%' }),
      e(TreeLight, { key: 'l2', top: '149px', left: '38.9%' }),
      e(TreeLight, { key: 'l3', top: '121px', left: '61.4%' }),
      e(TreeLight, { key: 'l4', top: '164px', left: '35.2%' }),
      e(TreeLight, { key: 'l5', top: '138px', left: '48.6%' }),
      e(TreeLight, { key: 'l6', top: '161px', left: '64.3%' }),
      e(TreeLight, { key: 'l7', top: '181px', left: '34.1%' }),
      e(TreeLight, { key: 'l8', top: '159px', left: '41.9%' }),
      e(TreeLight, { key: 'l9', top: '185px', left: '58.2%' }),
      e(TreeLight, { key: 'l10', top: '153px', left: '65.8%' }),
      
      e(TreeLight, { key: 'l11', top: '224px', left: '31.8%' }),
      e(TreeLight, { key: 'l12', top: '207px', left: '43.4%' }),
      e(TreeLight, { key: 'l13', top: '218px', left: '51.2%' }),
      e(TreeLight, { key: 'l14', top: '211px', left: '56.7%' }),
      e(TreeLight, { key: 'l15', top: '227px', left: '68.1%' }),
      e(TreeLight, { key: 'l16', top: '252px', left: '28.9%' }),
      e(TreeLight, { key: 'l17', top: '236px', left: '36.8%' }),
      e(TreeLight, { key: 'l18', top: '248px', left: '46.3%' }),
      e(TreeLight, { key: 'l19', top: '241px', left: '49.7%' }),
      e(TreeLight, { key: 'l20', top: '254px', left: '54.8%' }),
      e(TreeLight, { key: 'l21', top: '233px', left: '63.1%' }),
      e(TreeLight, { key: 'l22', top: '245px', left: '70.9%' }),
      e(TreeLight, { key: 'l23', top: '281px', left: '27.2%' }),
      e(TreeLight, { key: 'l24', top: '265px', left: '34.9%' }),
      e(TreeLight, { key: 'l25', top: '276px', left: '44.1%' }),
      e(TreeLight, { key: 'l26', top: '270px', left: '50.4%' }),
      e(TreeLight, { key: 'l27', top: '262px', left: '55.8%' }),
      e(TreeLight, { key: 'l28', top: '283px', left: '64.9%' }),
      e(TreeLight, { key: 'l29', top: '273px', left: '72.7%' }),
      e(TreeLight, { key: 'l30', top: '312px', left: '26.1%' }),
      e(TreeLight, { key: 'l31', top: '294px', left: '33.8%' }),
      e(TreeLight, { key: 'l32', top: '307px', left: '41.9%' }),
      e(TreeLight, { key: 'l33', top: '301px', left: '50.8%' }),
      e(TreeLight, { key: 'l34', top: '290px', left: '58.3%' }),
      e(TreeLight, { key: 'l35', top: '315px', left: '65.9%' }),
      e(TreeLight, { key: 'l36', top: '297px', left: '73.8%' }),
      
      e(TreeLight, { key: 'l39', top: '391px', left: '40.9%' }),
      e(TreeLight, { key: 'l40', top: '387px', left: '50.3%' }),
      e(TreeLight, { key: 'l41', top: '394px', left: '59.1%' }),
      e(TreeLight, { key: 'l44', top: '443px', left: '22.7%' }),
      e(TreeLight, { key: 'l45', top: '428px', left: '29.8%' }),
      e(TreeLight, { key: 'l46', top: '437px', left: '36.9%' }),
      e(TreeLight, { key: 'l47', top: '432px', left: '43.6%' }),
      e(TreeLight, { key: 'l48', top: '446px', left: '50.2%' }),
      e(TreeLight, { key: 'l49', top: '425px', left: '56.4%' }),
      e(TreeLight, { key: 'l50', top: '440px', left: '63.1%' }),
      e(TreeLight, { key: 'l51', top: '434px', left: '70.3%' }),
      e(TreeLight, { key: 'l52', top: '449px', left: '77.4%' }),
      e(TreeLight, { key: 'l53', top: '491px', left: '20.8%' }),
      e(TreeLight, { key: 'l54', top: '476px', left: '27.2%' }),
      e(TreeLight, { key: 'l55', top: '485px', left: '33.9%' }),
      e(TreeLight, { key: 'l56', top: '480px', left: '40.7%' }),
      e(TreeLight, { key: 'l57', top: '494px', left: '47.3%' }),
      e(TreeLight, { key: 'l58', top: '473px', left: '50.1%' }),
      e(TreeLight, { key: 'l59', top: '488px', left: '52.8%' }),
      e(TreeLight, { key: 'l60', top: '482px', left: '59.4%' }),
      e(TreeLight, { key: 'l61', top: '497px', left: '66.2%' }),
      e(TreeLight, { key: 'l62', top: '478px', left: '73.1%' }),
      e(TreeLight, { key: 'l63', top: '493px', left: '79.3%' }),
      e(TreeLight, { key: 'l64', top: '541px', left: '19.6%' }),
      e(TreeLight, { key: 'l65', top: '526px', left: '25.8%' }),
      e(TreeLight, { key: 'l66', top: '535px', left: '31.9%' }),
      e(TreeLight, { key: 'l67', top: '530px', left: '38.2%' }),
      e(TreeLight, { key: 'l68', top: '544px', left: '44.3%' }),
      e(TreeLight, { key: 'l69', top: '523px', left: '50.4%' }),
      e(TreeLight, { key: 'l70', top: '538px', left: '56.1%' }),
      e(TreeLight, { key: 'l71', top: '532px', left: '62.4%' }),
      e(TreeLight, { key: 'l72', top: '547px', left: '68.7%' }),
      e(TreeLight, { key: 'l73', top: '528px', left: '74.3%' }),
      e(TreeLight, { key: 'l74', top: '543px', left: '80.2%' }),
      e(TreeLight, { key: 'l75', top: '589px', left: '18.7%' }),
      e(TreeLight, { key: 'l76', top: '574px', left: '24.3%' }),
      e(TreeLight, { key: 'l77', top: '583px', left: '30.1%' }),
      e(TreeLight, { key: 'l78', top: '578px', left: '36.4%' }),
      e(TreeLight, { key: 'l79', top: '592px', left: '42.3%' }),
      e(TreeLight, { key: 'l80', top: '571px', left: '48.2%' }),
      e(TreeLight, { key: 'l81', top: '586px', left: '50.6%' }),
      e(TreeLight, { key: 'l82', top: '580px', left: '52.9%' }),
      e(TreeLight, { key: 'l83', top: '595px', left: '58.3%' }),
      e(TreeLight, { key: 'l84', top: '573px', left: '64.7%' }),
      e(TreeLight, { key: 'l85', top: '588px', left: '70.2%' }),
      e(TreeLight, { key: 'l86', top: '576px', left: '76.4%' }),
      e(TreeLight, { key: 'l87', top: '591px', left: '81.3%' }),
    ];

    return e('div', { style: styles.container },
      e(RudolphNotification, { show: showNotification }),
      e(SantaSled),
      e('div', { style: styles.scene },
        stars,
        e('div', { style: styles.moon }),
        e('div', { style: styles.mountain1 }),
        e('div', { style: styles.mountain2 }),
        e('div', { style: styles.ground }),
        landscapeTrees
      ),
      snowflakes,
      e('div', { style: styles.header }, ""),
      e('div', { style: styles.treeContainer },
        e('div', { style: styles.treeBackground },
            e('div', { style: styles.treeLayer1 }),
            e('div', { style: styles.treeLayer2 }),
            e('div', { style: styles.treeLayer3 }),
            e('div', { style: styles.treeTrunk })
        ),
        treeLights,
        treeElements
      )
    );
  };

  globalThis['Advent Calendar'] = AdventCalendarWidget;
  globalThis.AirflowPlugin = AdventCalendarWidget;
})();
