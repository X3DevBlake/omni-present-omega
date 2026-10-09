/**
 * ============================================================================
 * GOD'S EYE VIEW (GODSEYEVIEW) — PLANETARY 3D SPATIAL INTELLIGENCE ENGINE
 * ============================================================================
 * Unites Omni-Present Omega (OPO) & Omni Ecosystem with real-time geospatial
 * situational awareness: Satellites, ADS-B Flight Radar, Maritime AIS,
 * Seismic Sensors, OPO Physical Nodes, and SCION Subsea Fiber Cables.
 * ============================================================================
 */

(function () {
  'use strict';

  class GodsEyeViewEngine {
    constructor(canvasId) {
      this.canvas = document.getElementById(canvasId);
      if (!this.canvas) return;

      this.ctx = this.canvas.getContext('2d');
      this.width = 0;
      this.height = 0;
      this.dpr = Math.min(window.devicePixelRatio || 1, 2);

      // Camera & Orientation
      this.rotX = 0.25; // Pitch
      this.rotY = -0.5; // Yaw
      this.zoom = 1.0;
      this.targetZoom = 1.0;
      this.baseRadius = 220;

      // Interaction state
      this.isDragging = false;
      this.lastMouseX = 0;
      this.lastMouseY = 0;
      this.autoRotate = true;
      this.autoRotateSpeed = 0.0018;

      // Active layers
      this.layers = {
        satellites: true,
        flights: true,
        maritime: true,
        seismic: true,
        opoNodes: true,
        subseaCables: true,
        terminator: true,
        anomalyScan: true
      };

      // Selected / Locked Target
      this.selectedEntity = null;
      this.cockpitMode = false;

      // Time tracking
      this.lastTimestamp = performance.now();
      this.epochTime = Date.now();

      // Entity Databases
      this.initEntities();
      this.initEvents();
      this.resize();

      // Start animation loop
      requestAnimationFrame(this.render.bind(this));
    }

    initEntities() {
      // 1. OPO Global Physical Nodes & SCION Routers
      this.opoNodes = [
        { id: 'OPO-ZUR-01', name: 'Zurich Hermetic Root', lat: 47.3769, lon: 8.5417, type: 'core', peers: 128, latency: '1.2ms', status: 'SYNCHRONIZED' },
        { id: 'OPO-TYO-02', name: 'Tokyo Sensorium Edge', lat: 35.6762, lon: 139.6503, type: 'sensorium', peers: 94, latency: '4.8ms', status: 'SYNCHRONIZED' },
        { id: 'OPO-IAD-03', name: 'Virginia Global Fabric Hub', lat: 38.9072, lon: -77.0369, type: 'fabric', peers: 256, latency: '0.8ms', status: 'SYNCHRONIZED' },
        { id: 'OPO-SIN-04', name: 'Singapore Quantum Gateway', lat: 1.3521, lon: 103.8198, type: 'quantum', peers: 86, latency: '3.1ms', status: 'SYNCHRONIZED' },
        { id: 'OPO-FRA-05', name: 'Frankfurt SCION Router', lat: 50.1109, lon: 8.6821, type: 'scion', peers: 174, latency: '1.5ms', status: 'SYNCHRONIZED' },
        { id: 'OPO-SAO-06', name: 'São Paulo LatAm Mesh', lat: -23.5505, lon: -46.6333, type: 'sensorium', peers: 62, latency: '6.4ms', status: 'SYNCHRONIZED' },
        { id: 'OPO-SYD-07', name: 'Sydney Pacific Hub', lat: -33.8688, lon: 151.2093, type: 'fabric', peers: 78, latency: '5.2ms', status: 'SYNCHRONIZED' },
        { id: 'OPO-DXB-08', name: 'Dubai MENA Relay', lat: 25.2048, lon: 55.2708, type: 'core', peers: 92, latency: '2.9ms', status: 'SYNCHRONIZED' },
        { id: 'OPO-SFO-09', name: 'Silicon Valley Frontier Edge', lat: 37.7749, lon: -122.4194, type: 'core', peers: 210, latency: '1.1ms', status: 'SYNCHRONIZED' }
      ];

      // 2. Subsea Fiberoptic Cables connecting OPO Nodes
      this.cables = [
        { from: 'OPO-IAD-03', to: 'OPO-ZUR-01', name: 'TAT-14 Atlantic Express' },
        { from: 'OPO-ZUR-01', to: 'OPO-FRA-05', name: 'C-E-Connect Core' },
        { from: 'OPO-FRA-05', to: 'OPO-DXB-08', name: 'Euro-Asia Trans-Gulf' },
        { from: 'OPO-DXB-08', to: 'OPO-SIN-04', name: 'SEA-ME-WE 5' },
        { from: 'OPO-SIN-04', to: 'OPO-TYO-02', name: 'Asia-Pacific Gateway' },
        { from: 'OPO-TYO-02', to: 'OPO-SFO-09', name: 'FASTER Trans-Pacific' },
        { from: 'OPO-SFO-09', to: 'OPO-IAD-03', name: 'North American SCION Fiber' },
        { from: 'OPO-IAD-03', to: 'OPO-SAO-06', name: 'Monet Americas Trunk' },
        { from: 'OPO-SIN-04', to: 'OPO-SYD-07', name: 'Australia-Singapore Fiber' },
        { from: 'OPO-SYD-07', to: 'OPO-SFO-09', name: 'Southern Cross Next' }
      ];

      // 3. Orbital Satellites (TLE-based orbit propagation)
      this.satellites = [
        { id: 'SAT-25544', name: 'ISS (ZARYA)', alt: 420, inc: 51.6, speed: 7.66, phase: 0.8, color: '#38BDF8', type: 'orbital_station', apogee: '422 km', perigee: '418 km' },
        { id: 'SAT-STAR-01', name: 'STARLINK-9102', alt: 550, inc: 53.2, speed: 7.58, phase: 1.4, color: '#00E5FF', type: 'constellation', apogee: '553 km', perigee: '548 km' },
        { id: 'SAT-STAR-02', name: 'STARLINK-9108', alt: 550, inc: 53.2, speed: 7.58, phase: 2.9, color: '#00E5FF', type: 'constellation', apogee: '551 km', perigee: '549 km' },
        { id: 'SAT-GPS-07', name: 'GPS-III-07 (NAVSTAR)', alt: 20200, inc: 55.0, speed: 3.87, phase: 0.3, color: '#FFD700', type: 'navigation', apogee: '20,220 km', perigee: '20,180 km' },
        { id: 'SAT-KH11', name: 'USA-290 (KEYHOLE RECON)', alt: 380, inc: 97.4, speed: 7.72, phase: 4.1, color: '#F43F5E', type: 'surveillance', apogee: '395 km', perigee: '372 km' },
        { id: 'SAT-SENTINEL', name: 'SENTINEL-6A (COPERNICUS)', alt: 1336, inc: 66.0, speed: 7.15, phase: 3.5, color: '#4ADE80', type: 'earth_observatory', apogee: '1,340 km', perigee: '1,332 km' },
        { id: 'SAT-CSS', name: 'TIANGONG (CSS-3)', alt: 390, inc: 41.5, speed: 7.68, phase: 5.2, color: '#E040FB', type: 'orbital_station', apogee: '395 km', perigee: '388 km' }
      ];

      // 4. Real-Time ADS-B Aviation Flights
      this.flights = [
        { id: 'FLT-AF1', name: 'USAF FORTE12 (RQ-4B HAWK)', lat: 43.1, lon: 31.5, heading: 85, alt: '52,000 ft', speed: '340 kts', mach: '0.58', callsign: 'FORTE12', type: 'military_recon' },
        { id: 'FLT-RC135', name: 'USAF HOMER21 (RC-135W)', lat: 55.4, lon: 20.8, heading: 140, alt: '31,000 ft', speed: '465 kts', mach: '0.74', callsign: 'HOMER21', type: 'sigint' },
        { id: 'FLT-NATO01', name: 'NATO AWACS (E-3A)', lat: 51.2, lon: 23.4, heading: 220, alt: '29,000 ft', speed: '420 kts', mach: '0.69', callsign: 'NATO01', type: 'airborne_radar' },
        { id: 'FLT-BAW117', name: 'British Airways BAW117', lat: 48.8, lon: -35.2, heading: 260, alt: '38,000 ft', speed: '495 kts', mach: '0.84', callsign: 'BAW117', route: 'LHR → JFK', type: 'commercial' },
        { id: 'FLT-UAE201', name: 'Emirates UAE201', lat: 32.5, lon: 44.8, heading: 310, alt: '40,000 ft', speed: '510 kts', mach: '0.85', callsign: 'UAE201', route: 'DXB → JFK', type: 'commercial' },
        { id: 'FLT-SIA022', name: 'Singapore Airlines SIA22', lat: 18.2, lon: 115.4, heading: 45, alt: '36,000 ft', speed: '480 kts', mach: '0.82', callsign: 'SIA022', route: 'SIN → EWR', type: 'commercial' }
      ];

      // 5. Maritime AIS Vessels
      this.vessels = [
        { id: 'MAR-EVER', name: 'EVER GIVEN (Ultra-Large Container)', lat: 12.8, lon: 43.3, heading: 330, speed: '18.4 kts', destination: 'Rotterdam', cargo: '20,124 TEU', type: 'container' },
        { id: 'MAR-TANKER', name: 'TI EUROPE (ULCC Crude Supertanker)', lat: 24.5, lon: 58.2, heading: 125, speed: '14.1 kts', destination: 'Singapore', cargo: '3.1M bbl Crude', type: 'tanker' },
        { id: 'MAR-LNG', name: 'AL DAAYEN (Q-Flex LNG Carrier)', lat: 5.2, lon: 98.4, heading: 95, speed: '19.2 kts', destination: 'Tokyo Bay', cargo: '216,000 m³ LNG', type: 'lng' },
        { id: 'MAR-CVN78', name: 'USS GERALD R. FORD (CVN-78)', lat: 35.8, lon: 18.4, heading: 275, speed: '28.0 kts', destination: 'Eastern Med Patrol', type: 'naval_strike' },
        { id: 'MAR-NOAA', name: 'NOAA RONALD H. BROWN', lat: -15.4, lon: -110.2, heading: 190, speed: '11.5 kts', destination: 'Pacific Deep Hydrothermal Survey', type: 'research' }
      ];

      // 6. Seismic & Thermal Sensors
      this.seismic = [
        { id: 'EQ-01', name: 'Kuril Subduction Zone', lat: 46.2, lon: 153.4, mag: 6.8, depth: '35 km', time: '18m ago', status: 'ACTIVE_SHOCK' },
        { id: 'EQ-02', name: 'Mid-Atlantic Ridge Crest', lat: 0.8, lon: -28.4, mag: 5.4, depth: '10 km', time: '42m ago', status: 'STABLE' },
        { id: 'EQ-03', name: 'Tonga Kermadec Trench', lat: -21.4, lon: -175.2, mag: 7.2, depth: '62 km', time: '1h 12m ago', status: 'TSUNAMI_EVAL_CLEAR' }
      ];

      // Select default entity for HUD
      this.selectedEntity = this.opoNodes[0];
    }

    initEvents() {
      window.addEventListener('resize', this.resize.bind(this));

      // Pointer drag interaction
      const onPointerDown = (e) => {
        this.isDragging = true;
        this.lastMouseX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
        this.lastMouseY = e.clientY || (e.touches && e.touches[0].clientY) || 0;
        this.autoRotate = false;
      };

      const onPointerMove = (e) => {
        if (!this.isDragging) return;
        const clientX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
        const clientY = e.clientY || (e.touches && e.touches[0].clientY) || 0;

        const deltaX = clientX - this.lastMouseX;
        const deltaY = clientY - this.lastMouseY;

        this.rotY += deltaX * 0.006;
        this.rotX += deltaY * 0.006;

        // Clamp pitch to avoid gimbal flipping
        this.rotX = Math.max(-Math.PI / 2.2, Math.min(Math.PI / 2.2, this.rotX));

        this.lastMouseX = clientX;
        this.lastMouseY = clientY;
      };

      const onPointerUp = () => {
        this.isDragging = false;
      };

      this.canvas.addEventListener('mousedown', onPointerDown);
      window.addEventListener('mousemove', onPointerMove);
      window.addEventListener('mouseup', onPointerUp);

      this.canvas.addEventListener('touchstart', onPointerDown, { passive: true });
      window.addEventListener('touchmove', onPointerMove, { passive: true });
      window.addEventListener('touchend', onPointerUp);

      // Wheel Zoom
      this.canvas.addEventListener('wheel', (e) => {
        e.preventDefault();
        const zoomDelta = -e.deltaY * 0.0015;
        this.zoom = Math.max(0.65, Math.min(2.8, this.zoom + zoomDelta));
      }, { passive: false });

      // Click to target / select entity
      this.canvas.addEventListener('click', (e) => {
        const rect = this.canvas.getBoundingClientRect();
        const clickX = (e.clientX - rect.left) * this.dpr;
        const clickY = (e.clientY - rect.top) * this.dpr;
        this.handleClick(clickX, clickY);
      });
    }

    resize() {
      const parent = this.canvas.parentElement;
      if (!parent) return;

      this.width = parent.clientWidth;
      this.height = parent.clientHeight || 650;

      this.canvas.width = this.width * this.dpr;
      this.canvas.height = this.height * this.dpr;
      this.canvas.style.width = `${this.width}px`;
      this.canvas.style.height = `${this.height}px`;

      // Adaptive base radius
      this.baseRadius = Math.min(this.width, this.height) * 0.36;
    }

    // Convert LAT/LON to 3D Sphere Cartesian coordinates (x, y, z)
    latLonTo3D(lat, lon, altitudeRatio = 1.0) {
      const phi = (90 - lat) * (Math.PI / 180);
      const theta = (lon + 180) * (Math.PI / 180) + this.rotY;
      const radius = this.baseRadius * this.zoom * altitudeRatio;

      // 3D Cartesian coordinates
      let x = -(radius * Math.sin(phi) * Math.cos(theta));
      let z = (radius * Math.sin(phi) * Math.sin(theta));
      let y = (radius * Math.cos(phi));

      // Apply Pitch (rotX)
      const cosX = Math.cos(this.rotX);
      const sinX = Math.sin(this.rotX);

      const y1 = y * cosX - z * sinX;
      const z1 = y * sinX + z * cosX;

      // Project onto 2D Screen
      const centerX = (this.width * this.dpr) / 2;
      const centerY = (this.height * this.dpr) / 2;

      return {
        screenX: centerX + x,
        screenY: centerY - y1,
        zDepth: z1,
        visible: z1 > -20 // Visible on the front-facing hemisphere
      };
    }

    handleClick(x, y) {
      const candidates = [];

      // Check OPO Nodes
      this.opoNodes.forEach(node => {
        const pos = this.latLonTo3D(node.lat, node.lon);
        if (pos.visible) {
          const dist = Math.hypot(x - pos.screenX, y - pos.screenY);
          if (dist < 22 * this.dpr) candidates.push({ entity: node, dist, category: 'OPO_NODE' });
        }
      });

      // Check Flights
      this.flights.forEach(flight => {
        const pos = this.latLonTo3D(flight.lat, flight.lon, 1.04);
        if (pos.visible) {
          const dist = Math.hypot(x - pos.screenX, y - pos.screenY);
          if (dist < 22 * this.dpr) candidates.push({ entity: flight, dist, category: 'FLIGHT' });
        }
      });

      // Check Vessels
      this.vessels.forEach(vessel => {
        const pos = this.latLonTo3D(vessel.lat, vessel.lon, 1.01);
        if (pos.visible) {
          const dist = Math.hypot(x - pos.screenX, y - pos.screenY);
          if (dist < 22 * this.dpr) candidates.push({ entity: vessel, dist, category: 'VESSEL' });
        }
      });

      // Check Satellites
      this.satellites.forEach(sat => {
        const altRatio = 1.15 + (sat.alt / 15000);
        const lon = (sat.phase * 60 + (this.epochTime * 0.0001 * sat.speed)) % 360 - 180;
        const lat = Math.sin(sat.phase + this.epochTime * 0.00008) * sat.inc;
        const pos = this.latLonTo3D(lat, lon, altRatio);
        if (pos.visible) {
          const dist = Math.hypot(x - pos.screenX, y - pos.screenY);
          if (dist < 26 * this.dpr) candidates.push({ entity: sat, dist, category: 'SATELLITE' });
        }
      });

      if (candidates.length > 0) {
        candidates.sort((a, b) => a.dist - b.dist);
        this.selectTarget(candidates[0].entity, candidates[0].category);
      }
    }

    selectTarget(entity, category = 'ENTITY') {
      this.selectedEntity = entity;
      this.selectedCategory = category;

      // Update UI HUD if elements exist
      const titleElem = document.getElementById('godseye-hud-title');
      const metaElem = document.getElementById('godseye-hud-meta');
      const badgeElem = document.getElementById('godseye-hud-badge');

      if (titleElem) titleElem.textContent = entity.name || entity.id;
      if (badgeElem) badgeElem.textContent = category;
      if (metaElem) {
        if (category === 'OPO_NODE') {
          metaElem.innerHTML = `<strong>LAT/LON:</strong> ${entity.lat.toFixed(4)}°, ${entity.lon.toFixed(4)}° &bull; <strong>PEERS:</strong> ${entity.peers} &bull; <strong>RTT:</strong> ${entity.latency}`;
        } else if (category === 'FLIGHT') {
          metaElem.innerHTML = `<strong>CALLSIGN:</strong> ${entity.callsign} &bull; <strong>ALT:</strong> ${entity.alt} &bull; <strong>SPEED:</strong> ${entity.speed} (${entity.mach}) &bull; <strong>HDG:</strong> ${entity.heading}°`;
        } else if (category === 'VESSEL') {
          metaElem.innerHTML = `<strong>TYPE:</strong> ${entity.type.toUpperCase()} &bull; <strong>DEST:</strong> ${entity.destination} &bull; <strong>SPEED:</strong> ${entity.speed} &bull; <strong>CARGO:</strong> ${entity.cargo || 'Classified'}`;
        } else if (category === 'SATELLITE') {
          metaElem.innerHTML = `<strong>ORBIT:</strong> ${entity.apogee} &times; ${entity.perigee} &bull; <strong>VELOCITY:</strong> ${entity.speed} km/s &bull; <strong>INC:</strong> ${entity.inc}°`;
        }
      }

      if (window.soundEngine) window.soundEngine.playClick();
    }

    render(timestamp) {
      const dt = (timestamp - this.lastTimestamp) / 1000;
      this.lastTimestamp = timestamp;
      this.epochTime += dt * 1000;

      // Auto-rotation if user is not dragging
      if (this.autoRotate) {
        this.rotY += this.autoRotateSpeed;
      }

      const ctx = this.ctx;
      const w = this.width * this.dpr;
      const h = this.height * this.dpr;
      const cx = w / 2;
      const cy = h / 2;
      const r = this.baseRadius * this.zoom;

      ctx.clearRect(0, 0, w, h);

      // 1. Atmospheric Glow / Starfield Halo
      const glowGrad = ctx.createRadialGradient(cx, cy, r * 0.85, cx, cy, r * 1.35);
      glowGrad.addColorStop(0, 'rgba(0, 229, 255, 0.12)');
      glowGrad.addColorStop(0.5, 'rgba(59, 130, 246, 0.05)');
      glowGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = glowGrad;
      ctx.beginPath();
      ctx.arc(cx, cy, r * 1.35, 0, Math.PI * 2);
      ctx.fill();

      // 2. Earth Sphere Base (Deep Space Obsidian Glass)
      const sphereGrad = ctx.createRadialGradient(cx - r * 0.35, cy - r * 0.35, r * 0.1, cx, cy, r);
      sphereGrad.addColorStop(0, 'rgba(20, 30, 48, 0.95)');
      sphereGrad.addColorStop(0.7, 'rgba(10, 15, 25, 0.98)');
      sphereGrad.addColorStop(1, 'rgba(3, 7, 18, 1)');

      ctx.fillStyle = sphereGrad;
      ctx.beginPath();
      ctx.arc(cx, cy, r, 0, Math.PI * 2);
      ctx.fill();

      // Earth Sphere Rim Border
      ctx.strokeStyle = 'rgba(0, 229, 255, 0.4)';
      ctx.lineWidth = 1.5 * this.dpr;
      ctx.stroke();

      // 3. Latitude & Longitude Coordinate Wireframe Grid
      this.drawCoordinateGrid(ctx, cx, cy, r);

      // 4. Subsea Fiber Cables Layer
      if (this.layers.subseaCables) {
        this.drawSubseaCables(ctx);
      }

      // 5. Seismic Shockwaves Layer
      if (this.layers.seismic) {
        this.drawSeismicEvents(ctx);
      }

      // 6. Maritime AIS Fleet
      if (this.layers.maritime) {
        this.drawMaritimeFleet(ctx);
      }

      // 7. Global ADS-B Flights
      if (this.layers.flights) {
        this.drawFlights(ctx);
      }

      // 8. OPO Physical Nodes & SCION Gateways
      if (this.layers.opoNodes) {
        this.drawOpoNodes(ctx);
      }

      // 9. Orbital Satellite Trajectories & Constellations
      if (this.layers.satellites) {
        this.drawSatellites(ctx);
      }

      // 10. Selected Target HUD Reticle
      if (this.selectedEntity) {
        this.drawTargetReticle(ctx);
      }

      // 11. Scanner Beam Line
      this.drawScanline(ctx, cx, cy, r);

      requestAnimationFrame(this.render.bind(this));
    }

    drawCoordinateGrid(ctx, cx, cy, r) {
      ctx.strokeStyle = 'rgba(0, 229, 255, 0.08)';
      ctx.lineWidth = 1 * this.dpr;

      // Parallels (Latitudes: -60, -30, 0, 30, 60)
      [-60, -30, 0, 30, 60].forEach(lat => {
        ctx.beginPath();
        let started = false;
        for (let lon = -180; lon <= 180; lon += 5) {
          const pt = this.latLonTo3D(lat, lon);
          if (pt.visible) {
            if (!started) {
              ctx.moveTo(pt.screenX, pt.screenY);
              started = true;
            } else {
              ctx.lineTo(pt.screenX, pt.screenY);
            }
          } else {
            started = false;
          }
        }
        ctx.stroke();
      });

      // Meridians (Longitudes every 30 degrees)
      for (let lon = -180; lon < 180; lon += 30) {
        ctx.beginPath();
        let started = false;
        for (let lat = -80; lat <= 80; lat += 5) {
          const pt = this.latLonTo3D(lat, lon);
          if (pt.visible) {
            if (!started) {
              ctx.moveTo(pt.screenX, pt.screenY);
              started = true;
            } else {
              ctx.lineTo(pt.screenX, pt.screenY);
            }
          } else {
            started = false;
          }
        }
        ctx.stroke();
      }
    }

    drawSubseaCables(ctx) {
      ctx.save();
      this.cables.forEach(cable => {
        const fromNode = this.opoNodes.find(n => n.id === cable.from);
        const toNode = this.opoNodes.find(n => n.id === cable.to);
        if (!fromNode || !toNode) return;

        // Sample great circle arc
        ctx.beginPath();
        let started = false;
        let visibleCount = 0;
        const steps = 24;

        for (let i = 0; i <= steps; i++) {
          const t = i / steps;
          const lat = fromNode.lat + (toNode.lat - fromNode.lat) * t;
          let lon = fromNode.lon + (toNode.lon - fromNode.lon) * t;

          // Great circle curvature adjustment
          const midArc = Math.sin(t * Math.PI) * 4;
          const pt = this.latLonTo3D(lat + midArc, lon, 1.002);

          if (pt.visible) {
            visibleCount++;
            if (!started) {
              ctx.moveTo(pt.screenX, pt.screenY);
              started = true;
            } else {
              ctx.lineTo(pt.screenX, pt.screenY);
            }
          } else {
            started = false;
          }
        }

        if (visibleCount > 2) {
          ctx.strokeStyle = 'rgba(0, 229, 255, 0.35)';
          ctx.lineWidth = 1.2 * this.dpr;
          ctx.setLineDash([4 * this.dpr, 3 * this.dpr]);
          ctx.stroke();
          ctx.setLineDash([]);
        }
      });
      ctx.restore();
    }

    drawSeismicEvents(ctx) {
      this.seismic.forEach(eq => {
        const pt = this.latLonTo3D(eq.lat, eq.lon);
        if (!pt.visible) return;

        const pulse = (this.epochTime * 0.002) % 1;
        const ringRadius = (eq.mag * 3 + pulse * 18) * this.dpr;
        const alpha = Math.max(0, 1 - pulse) * 0.8;

        ctx.strokeStyle = `rgba(244, 63, 94, ${alpha})`;
        ctx.lineWidth = 1.8 * this.dpr;
        ctx.beginPath();
        ctx.arc(pt.screenX, pt.screenY, ringRadius, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = '#F43F5E';
        ctx.beginPath();
        ctx.arc(pt.screenX, pt.screenY, 3 * this.dpr, 0, Math.PI * 2);
        ctx.fill();

        // Label
        ctx.fillStyle = '#FDA4AF';
        ctx.font = `${9 * this.dpr}px JetBrains Mono, monospace`;
        ctx.fillText(`M${eq.mag}`, pt.screenX + 6 * this.dpr, pt.screenY - 4 * this.dpr);
      });
    }

    drawMaritimeFleet(ctx) {
      this.vessels.forEach(v => {
        // Slow movement simulation
        const curLon = v.lon + Math.sin(this.epochTime * 0.00005) * 0.5;
        const pt = this.latLonTo3D(v.lat, curLon, 1.008);
        if (!pt.visible) return;

        ctx.fillStyle = '#38BDF8';
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.5)';
        ctx.lineWidth = 1 * this.dpr;

        // Boat icon (diamond shape)
        ctx.beginPath();
        ctx.moveTo(pt.screenX, pt.screenY - 4 * this.dpr);
        ctx.lineTo(pt.screenX + 3 * this.dpr, pt.screenY);
        ctx.lineTo(pt.screenX, pt.screenY + 4 * this.dpr);
        ctx.lineTo(pt.screenX - 3 * this.dpr, pt.screenY);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = 'rgba(224, 242, 254, 0.8)';
        ctx.font = `${8 * this.dpr}px JetBrains Mono, monospace`;
        ctx.fillText(v.name.split(' ')[0], pt.screenX + 6 * this.dpr, pt.screenY + 3 * this.dpr);
      });
    }

    drawFlights(ctx) {
      this.flights.forEach(f => {
        // Aircraft vector simulation
        const curLon = f.lon + (this.epochTime * 0.00015 * (f.speed.includes('4') ? 1 : 1.5)) % 60 - 30;
        const pt = this.latLonTo3D(f.lat, curLon, 1.035);
        if (!pt.visible) return;

        const isMilitary = f.type.includes('military') || f.type.includes('sigint');
        ctx.fillStyle = isMilitary ? '#F59E0B' : '#60A5FA';

        // Jet aircraft chevron
        ctx.beginPath();
        ctx.arc(pt.screenX, pt.screenY, 3 * this.dpr, 0, Math.PI * 2);
        ctx.fill();

        // Heading vector velocity line
        const hdgRad = (f.heading - 90) * (Math.PI / 180);
        ctx.strokeStyle = isMilitary ? 'rgba(245, 158, 11, 0.7)' : 'rgba(96, 165, 250, 0.7)';
        ctx.lineWidth = 1.2 * this.dpr;
        ctx.beginPath();
        ctx.moveTo(pt.screenX, pt.screenY);
        ctx.lineTo(pt.screenX + Math.cos(hdgRad) * 12 * this.dpr, pt.screenY + Math.sin(hdgRad) * 12 * this.dpr);
        ctx.stroke();

        ctx.fillStyle = isMilitary ? '#FDE68A' : '#BFDBFE';
        ctx.font = `${8 * this.dpr}px JetBrains Mono, monospace`;
        ctx.fillText(f.callsign, pt.screenX + 6 * this.dpr, pt.screenY - 5 * this.dpr);
      });
    }

    drawOpoNodes(ctx) {
      this.opoNodes.forEach(n => {
        const pt = this.latLonTo3D(n.lat, n.lon, 1.015);
        if (!pt.visible) return;

        // Glowing node halo
        ctx.fillStyle = 'rgba(0, 229, 255, 0.3)';
        ctx.beginPath();
        ctx.arc(pt.screenX, pt.screenY, 7 * this.dpr, 0, Math.PI * 2);
        ctx.fill();

        // Node center jewel
        ctx.fillStyle = '#00E5FF';
        ctx.beginPath();
        ctx.arc(pt.screenX, pt.screenY, 3.5 * this.dpr, 0, Math.PI * 2);
        ctx.fill();

        // Label
        ctx.fillStyle = '#FFFFFF';
        ctx.font = `bold ${8.5 * this.dpr}px JetBrains Mono, monospace`;
        ctx.fillText(n.id, pt.screenX + 8 * this.dpr, pt.screenY + 3 * this.dpr);
      });
    }

    drawSatellites(ctx) {
      this.satellites.forEach(s => {
        const altRatio = 1.14 + (s.alt / 18000);
        const lon = (s.phase * 50 + (this.epochTime * 0.00012 * s.speed)) % 360 - 180;
        const lat = Math.sin(s.phase + this.epochTime * 0.00008) * s.inc;
        const pt = this.latLonTo3D(lat, lon, altRatio);

        if (pt.visible) {
          // Orbit trace trail
          ctx.strokeStyle = s.color || '#38BDF8';
          ctx.fillStyle = s.color || '#38BDF8';

          // Satellite solar panel box icon
          ctx.fillRect(pt.screenX - 3 * this.dpr, pt.screenY - 2 * this.dpr, 6 * this.dpr, 4 * this.dpr);

          // Solar panel wing lines
          ctx.lineWidth = 1 * this.dpr;
          ctx.beginPath();
          ctx.moveTo(pt.screenX - 7 * this.dpr, pt.screenY);
          ctx.lineTo(pt.screenX + 7 * this.dpr, pt.screenY);
          ctx.stroke();

          // Label
          ctx.fillStyle = '#E2E8F0';
          ctx.font = `${8 * this.dpr}px JetBrains Mono, monospace`;
          ctx.fillText(s.name, pt.screenX + 8 * this.dpr, pt.screenY - 4 * this.dpr);
        }
      });
    }

    drawTargetReticle(ctx) {
      const e = this.selectedEntity;
      let lat = e.lat || 0;
      let lon = e.lon || 0;
      let alt = 1.015;

      if (e.alt && typeof e.alt === 'number') {
        alt = 1.14 + (e.alt / 18000);
      }

      const pt = this.latLonTo3D(lat, lon, alt);
      if (!pt.visible) return;

      const size = 16 * this.dpr;
      ctx.strokeStyle = 'rgba(0, 229, 255, 0.9)';
      ctx.lineWidth = 1.5 * this.dpr;

      // Crosshair corners
      ctx.beginPath();
      // Top-Left
      ctx.moveTo(pt.screenX - size, pt.screenY - size / 2);
      ctx.lineTo(pt.screenX - size, pt.screenY - size);
      ctx.lineTo(pt.screenX - size / 2, pt.screenY - size);

      // Top-Right
      ctx.moveTo(pt.screenX + size / 2, pt.screenY - size);
      ctx.lineTo(pt.screenX + size, pt.screenY - size);
      ctx.lineTo(pt.screenX + size, pt.screenY - size / 2);

      // Bottom-Left
      ctx.moveTo(pt.screenX - size, pt.screenY + size / 2);
      ctx.lineTo(pt.screenX - size, pt.screenY + size);
      ctx.lineTo(pt.screenX - size / 2, pt.screenY + size);

      // Bottom-Right
      ctx.moveTo(pt.screenX + size / 2, pt.screenY + size);
      ctx.lineTo(pt.screenX + size, pt.screenY + size);
      ctx.lineTo(pt.screenX + size, pt.screenY + size / 2);
      ctx.stroke();
    }

    drawScanline(ctx, cx, cy, r) {
      const scanY = cy + Math.sin(this.epochTime * 0.001) * r * 0.95;
      const xSpan = Math.sqrt(Math.max(0, r * r - (scanY - cy) * (scanY - cy)));

      const grad = ctx.createLinearGradient(cx - xSpan, scanY, cx + xSpan, scanY);
      grad.addColorStop(0, 'rgba(0, 229, 255, 0)');
      grad.addColorStop(0.5, 'rgba(0, 229, 255, 0.4)');
      grad.addColorStop(1, 'rgba(0, 229, 255, 0)');

      ctx.strokeStyle = grad;
      ctx.lineWidth = 1.5 * this.dpr;
      ctx.beginPath();
      ctx.moveTo(cx - xSpan, scanY);
      ctx.lineTo(cx + xSpan, scanY);
      ctx.stroke();
    }
  }

  // Auto-initialize when canvas is loaded
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('godseye-globe-canvas')) {
      window.godsEyeEngine = new GodsEyeViewEngine('godseye-globe-canvas');
    }
  });

})();
