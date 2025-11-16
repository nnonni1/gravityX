
[index.html](https://github.com/user-attachments/files/23567260/index.html)
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gravity X - Mission Control Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
            color: #e0e6ed;
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* ═══════════════════════════════════════════════════════ */
        /*                      HEADER                           */
        /* ═══════════════════════════════════════════════════════ */
        .header {
            background: linear-gradient(90deg, #1e3a5f 0%, #2d4a6f 100%);
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            border-bottom: 3px solid #4a9eff;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .logo h1 {
            font-size: 32px;
            font-weight: 700;
            background: linear-gradient(90deg, #4a9eff, #00d4ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(74, 158, 255, 0.5);
        }

        .logo-icon {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #4a9eff, #00d4ff);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            box-shadow: 0 0 20px rgba(74, 158, 255, 0.6);
            animation: rotate 10s linear infinite;
        }

        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .nav-menu {
            display: flex;
            gap: 20px;
        }

        .nav-btn {
            padding: 12px 25px;
            background: rgba(74, 158, 255, 0.1);
            border: 2px solid #4a9eff;
            border-radius: 8px;
            color: #4a9eff;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: 600;
        }

        .nav-btn:hover, .nav-btn.active {
            background: #4a9eff;
            color: white;
            box-shadow: 0 0 20px rgba(74, 158, 255, 0.6);
        }

        .system-status {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 20px;
            background: rgba(0, 212, 106, 0.1);
            border: 2px solid #00d46a;
            border-radius: 8px;
        }

        .status-indicator {
            width: 12px;
            height: 12px;
            background: #00d46a;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
        }

        /* ═══════════════════════════════════════════════════════ */
        /*                   MAIN CONTAINER                      */
        /* ═══════════════════════════════════════════════════════ */
        .container {
            padding: 30px;
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 30px;
        }

        /* ═══════════════════════════════════════════════════════ */
        /*                   CONTROL PANEL                       */
        /* ═══════════════════════════════════════════════════════ */
        .control-panel {
            background: rgba(30, 58, 95, 0.4);
            border: 2px solid #4a9eff;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
        }

        .panel-title {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 25px;
            color: #4a9eff;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .mission-controls {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }

        .btn {
            padding: 15px 30px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }

        .btn-green {
            background: linear-gradient(135deg, #00d46a, #00a854);
            color: white;
        }

        .btn-green:hover {
            box-shadow: 0 0 30px rgba(0, 212, 106, 0.8);
            transform: translateY(-3px);
        }

        .btn-blue {
            background: linear-gradient(135deg, #4a9eff, #0066cc);
            color: white;
        }

        .btn-blue:hover {
            box-shadow: 0 0 30px rgba(74, 158, 255, 0.8);
            transform: translateY(-3px);
        }

        .btn-red {
            background: linear-gradient(135deg, #ff4757, #cc0000);
            color: white;
            font-size: 18px;
            padding: 18px 35px;
        }

        .btn-red:hover {
            box-shadow: 0 0 40px rgba(255, 71, 87, 0.9);
            transform: scale(1.05);
            animation: shake 0.3s;
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            75% { transform: translateX(5px); }
        }

        /* ═══════════════════════════════════════════════════════ */
        /*                  ROTATION VISUAL                      */
        /* ═══════════════════════════════════════════════════════ */
        .rotation-display {
            position: relative;
            width: 100%;
            height: 300px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            margin: 30px 0;
            overflow: hidden;
            border: 2px solid #4a9eff;
        }

        .rotation-path {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 250px;
            height: 250px;
            border: 3px dashed #4a9eff;
            border-radius: 50%;
            transform: translate(-50%, -50%);
            animation: rotateCircle 8s linear infinite;
        }

        @keyframes rotateCircle {
            from { transform: translate(-50%, -50%) rotate(0deg); }
            to { transform: translate(-50%, -50%) rotate(360deg); }
        }

        .point {
            position: absolute;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            border: 3px solid white;
        }

        .point-a {
            background: #00d46a;
            top: 10%;
            left: 50%;
            transform: translateX(-50%);
            box-shadow: 0 0 20px #00d46a;
        }

        .point-b {
            background: #ff4757;
            bottom: 10%;
            left: 50%;
            transform: translateX(-50%);
            box-shadow: 0 0 20px #ff4757;
        }

        .capsule {
            position: absolute;
            width: 30px;
            height: 30px;
            background: linear-gradient(135deg, #ffd700, #ffaa00);
            border-radius: 50%;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            box-shadow: 0 0 30px rgba(255, 215, 0, 0.8);
            animation: moveCapsule 4s ease-in-out infinite;
        }

        @keyframes moveCapsule {
            0%, 100% { transform: translate(-50%, -50%) translateY(-100px); }
            50% { transform: translate(-50%, -50%) translateY(100px); }
        }

        /* ═══════════════════════════════════════════════════════ */
        /*                     TELEMETRY                         */
        /* ═══════════════════════════════════════════════════════ */
        .telemetry-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .telemetry-card {
            background: linear-gradient(135deg, rgba(74, 158, 255, 0.1), rgba(0, 212, 255, 0.1));
            border: 2px solid #4a9eff;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            transition: all 0.3s;
        }

        .telemetry-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(74, 158, 255, 0.4);
        }

        .telemetry-label {
            font-size: 14px;
            color: #8b98a8;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .telemetry-value {
            font-size: 36px;
            font-weight: 700;
            color: #4a9eff;
            text-shadow: 0 0 10px rgba(74, 158, 255, 0.5);
        }

        .telemetry-unit {
            font-size: 16px;
            color: #8b98a8;
            margin-right: 5px;
        }

        /* ═══════════════════════════════════════════════════════ */
        /*                   HAZARDS PANEL                       */
        /* ═══════════════════════════════════════════════════════ */
        .hazards-panel {
            background: rgba(30, 58, 95, 0.4);
            border: 2px solid #ff4757;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
        }

        .hazard-item {
            background: rgba(255, 71, 87, 0.1);
            border: 2px solid;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 15px;
            transition: all 0.3s;
        }

        .hazard-item:hover {
            transform: translateX(-5px);
            box-shadow: 0 5px 20px rgba(255, 71, 87, 0.4);
        }

        .hazard-item.moderate {
            border-color: #ffa502;
            background: rgba(255, 165, 2, 0.1);
        }

        .hazard-item.high {
            border-color: #ff4757;
            animation: alertPulse 2s infinite;
        }

        @keyframes alertPulse {
            0%, 100% { box-shadow: 0 0 10px rgba(255, 71, 87, 0.5); }
            50% { box-shadow: 0 0 30px rgba(255, 71, 87, 1); }
        }

        .hazard-icon {
            font-size: 32px;
        }

        .hazard-info {
            flex: 1;
        }

        .hazard-name {
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 5px;
        }

        .hazard-severity {
            font-size: 14px;
            padding: 5px 15px;
            border-radius: 20px;
            display: inline-block;
            font-weight: 700;
        }

        .severity-moderate {
            background: #ffa502;
            color: white;
        }

        .severity-high {
            background: #ff4757;
            color: white;
        }

        .hazard-actions {
            display: flex;
            gap: 10px;
            flex-direction: column;
        }

        .btn-action {
            padding: 8px 20px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid white;
            border-radius: 6px;
            color: white;
            cursor: pointer;
            font-size: 12px;
            font-weight: 600;
            transition: all 0.3s;
        }

        .btn-action:hover {
            background: white;
            color: #1e3a5f;
        }

        /* ═══════════════════════════════════════════════════════ */
        /*               TRANSITION CHAMBER                      */
        /* ═══════════════════════════════════════════════════════ */
        .chamber-panel {
            background: rgba(30, 58, 95, 0.4);
            border: 2px solid #00d46a;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
            margin-top: 30px;
        }

        .chamber-visual {
            position: relative;
            width: 100%;
            height: 200px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            margin: 20px 0;
            overflow: hidden;
            border: 2px solid #00d46a;
        }

        .chamber-cylinder {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 150px;
            height: 150px;
            border: 3px solid #00d46a;
            border-radius: 50%;
            box-shadow: 0 0 30px rgba(0, 212, 106, 0.3);
        }

        .chamber-inner {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 90px;
            height: 90px;
            border: 3px solid #4a9eff;
            border-radius: 50%;
            background: rgba(74, 158, 255, 0.1);
            animation: rotateInner 3s linear infinite;
        }

        @keyframes rotateInner {
            from { transform: translate(-50%, -50%) rotate(0deg); }
            to { transform: translate(-50%, -50%) rotate(360deg); }
        }

        .chamber-controls {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }

        /* ═══════════════════════════════════════════════════════ */
        /*                  ENERGY DISPLAY                       */
        /* ═══════════════════════════════════════════════════════ */
        .energy-panel {
            background: rgba(30, 58, 95, 0.4);
            border: 2px solid #ffd700;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
        }

        .energy-bar {
            width: 100%;
            height: 40px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 20px;
            overflow: hidden;
            margin: 20px 0;
            border: 2px solid #ffd700;
        }

        .energy-fill {
            height: 100%;
            background: linear-gradient(90deg, #ffd700, #ffaa00);
            width: 73%;
            transition: width 1s;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.8);
            animation: energyPulse 2s infinite;
        }

        @keyframes energyPulse {
            0%, 100% { opacity: 0.8; }
            50% { opacity: 1; }
        }

        .energy-stats {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 20px;
        }

        .energy-stat {
            background: rgba(0, 0, 0, 0.3);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #ffd700;
        }

        .energy-stat-label {
            font-size: 12px;
            color: #8b98a8;
            margin-bottom: 5px;
        }

        .energy-stat-value {
            font-size: 24px;
            font-weight: 700;
            color: #ffd700;
        }

        /* ═══════════════════════════════════════════════════════ */
        /*                   RESPONSIVE                          */
        /* ═══════════════════════════════════════════════════════ */
        @media (max-width: 1024px) {
            .container {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 768px) {
            .header {
                flex-direction: column;
                gap: 20px;
            }

            .nav-menu {
                flex-direction: column;
                width: 100%;
            }

            .mission-controls {
                flex-direction: column;
            }

            .telemetry-grid {
                grid-template-columns: 1fr 1fr;
            }
        }
    </style>
</head>
<body>

    <!-- ═══════════════════════════════════════════════════════ -->
    <!--                        HEADER                         -->
    <!-- ═══════════════════════════════════════════════════════ -->
    <header class="header">
        <div class="logo">
            <div class="logo-icon">🛸</div>
            <h1>Gravity X</h1>
        </div>
        <nav class="nav-menu">
            <button class="nav-btn active">الرئيسية</button>
            <button class="nav-btn">التتبع</button>
            <button class="nav-btn">المخاطر</button>
            <button class="nav-btn">الطاقة</button>
        </nav>
        <div class="system-status">
            <div class="status-indicator"></div>
            <span>النظام نشط</span>
        </div>
    </header>

    <!-- ═══════════════════════════════════════════════════════ -->
    <!--                   MAIN CONTAINER                      -->
    <!-- ═══════════════════════════════════════════════════════ -->
    <div class="container">
        
        <!-- LEFT COLUMN -->
        <div>
            <!-- CONTROL PANEL -->
            <div class="control-panel">
                <h2 class="panel-title">🎮 لوحة التحكم الرئيسية</h2>
                
                <div class="mission-controls">
                    <button class="btn btn-green" onclick="startMission()">بدء المهمة</button>
                    <button class="btn btn-blue" onclick="autoTrack()">تتبع تلقائي</button>
                    <button class="btn btn-red" onclick="emergencyStop()">⚠️ إيقاف طارئ</button>
                </div>

                <!-- ROTATION DISPLAY -->
                <div class="rotation-display">
                    <div class="rotation-path"></div>
                    <div class="point point-a"></div>
                    <div class="point point-b"></div>
                    <div class="capsule"></div>
                </div>

                <!-- TELEMETRY -->
                <div class="telemetry-grid">
                    <div class="telemetry-card">
                        <div class="telemetry-label">RPM A</div>
                        <div class="telemetry-value"><span id="rpm-a">54</span></div>
                    </div>
                    <div class="telemetry-card">
                        <div class="telemetry-label">RPM B</div>
                        <div class="telemetry-value"><span id="rpm-b">54</span></div>
                    </div>
                    <div class="telemetry-card">
                        <div class="telemetry-label">Δθ</div>
                        <div class="telemetry-value"><span id="delta-theta">2</span><span class="telemetry-unit">°</span></div>
                    </div>
                    <div class="telemetry-card">
                        <div class="telemetry-label">المسافة</div>
                        <div class="telemetry-value"><span id="distance">13.2</span><span class="telemetry-unit">م</span></div>
                    </div>
                    <div class="telemetry-card">
                        <div class="telemetry-label">الفتحة</div>
                        <div class="telemetry-value"><span id="slot">1</span></div>
                    </div>
                    <div class="telemetry-card">
                        <div class="telemetry-label">الحالة</div>
                        <div class="telemetry-value" style="font-size: 18px; color: #00d46a;">نشط</div>
                    </div>
                </div>
            </div>

            <!-- TRANSITION CHAMBER -->
            <div class="chamber-panel">
                <h2 class="panel-title">🔄 غرفة الانتقال</h2>
                
                <div class="chamber-visual">
                    <div class="chamber-cylinder"></div>
                    <div class="chamber-inner"></div>
                </div>

                <div class="chamber-controls">
                    <button class="btn btn-blue" onclick="alignChamber()">محاذاة</button>
                    <button class="btn btn-green" onclick="holdSync()">تثبيت المزامنة</button>
                    <button class="btn btn-blue" onclick="releaseBall()">إطلاق الكبسولة</button>
                </div>

                <div class="telemetry-grid" style="margin-top: 20px;">
                    <div class="telemetry-card">
                        <div class="telemetry-label">المسافة</div>
                        <div class="telemetry-value" style="font-size: 24px;"><span id="chamber-dist">8.72</span><span class="telemetry-unit">م</span></div>
                    </div>
                    <div class="telemetry-card">
                        <div class="telemetry-label">زاوية المحاذاة</div>
                        <div class="telemetry-value" style="font-size: 24px;"><span id="chamber-angle">0</span><span class="telemetry-unit">°</span></div>
                    </div>
                    <div class="telemetry-card">
                        <div class="telemetry-label">RPM الداخلي</div>
                        <div class="telemetry-value" style="font-size: 24px;"><span id="chamber-rpm">30</span></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- RIGHT COLUMN -->
        <div>
            <!-- HAZARDS PANEL -->
            <div class="hazards-panel">
                <h2 class="panel-title">⚠️ المخاطر المكتشفة</h2>

                <div class="hazard-item moderate">
                    <div class="hazard-icon">⚠️</div>
                    <div class="hazard-info">
                        <div class="hazard-name">عائق في المسار</div>
                        <span class="hazard-severity severity-moderate">متوسط</span>
                    </div>
                    <div class="hazard-actions">
                        <button class="btn-action" onclick="stopMovement()">إيقاف</button>
                        <button class="btn-action" onclick="reroute()">إعادة توجيه</button>
                    </div>
                </div>

                <div class="hazard-item moderate">
                    <div class="hazard-icon">🔄</div>
                    <div class="hazard-info">
                        <div class="hazard-name">انحراف المسار</div>
                        <span class="hazard-severity severity-moderate">متوسط</span>
                    </div>
                    <div class="hazard-actions">
                        <button class="btn-action" onclick="stopMovement()">إيقاف</button>
                        <button class="btn-action" onclick="correctPath()">تصحيح</button>
                    </div>
                </div>

                <div class="hazard-item high">
                    <div class="hazard-icon">🔥</div>
                    <div class="hazard-info">
                        <div class="hazard-name">حريق مكتشف</div>
                        <span class="hazard-severity severity-high">عالي!</span>
                    </div>
                    <div class="hazard-actions">
                        <button class="btn-action" onclick="emergencyStop()">إيقاف فوري</button>
                        <button class="btn-action" onclick="dischargeCO2()">تفريغ CO₂</button>
                    </div>
                </div>
            </div>

            <!-- ENERGY PANEL -->
            <div class="energy-panel" style="margin-top: 30px;">
                <h2 class="panel-title">⚡ نظام استرجاع الطاقة البيزوإلكتريك</h2>
                
                <div class="energy-bar">
                    <div class="energy-fill" id="energy-fill"></div>
                </div>

                <div class="energy-stats">
                    <div class="energy-stat">
                        <div class="energy-stat-label">الجهد الحالي</div>
                        <div class="energy-stat-value"><span id="voltage">4.23</span> V</div>
                    </div>
                    <div class="energy-stat">
                        <div class="energy-stat-label">الطاقة المخزنة</div>
                        <div class="energy-stat-value"><span id="stored-energy">89.5</span> J</div>
                    </div>
                    <div class="energy-stat">
                        <div class="energy-stat-label">الطاقة التراكمية</div>
                        <div class="energy-stat-value"><span id="cumulative-energy">345</span> J</div>
                    </div>
                    <div class="energy-stat">
                        <div class="energy-stat-label">القدرة المتوسطة</div>
                        <div class="energy-stat-value"><span id="avg-power">27.2</span> μW</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- ═══════════════════════════════════════════════════════ -->
    <!--                      JAVASCRIPT                       -->
    <!-- ═══════════════════════════════════════════════════════ -->
    <script>
        // ═════════════════════════════════════════════════════
        //              SIMULATED TELEMETRY DATA
        // ═════════════════════════════════════════════════════
        function updateTelemetry() {
            // RPM values
            document.getElementById('rpm-a').innerText = Math.floor(Math.random() * 10 + 50);
            document.getElementById('rpm-b').innerText = Math.floor(Math.random() * 10 + 50);
            
            // Delta theta
            document.getElementById('delta-theta').innerText = Math.floor(Math.random() * 5 + 1);
            
            // Distance
            document.getElementById('distance').innerText = (Math.random() * 5 + 10).toFixed(1);
            
            // Slot
            document.getElementById('slot').innerText = Math.floor(Math.random() * 3 + 1);
            
            // Chamber telemetry
            document.getElementById('chamber-dist').innerText = (Math.random() * 3 + 7).toFixed(2);
            document.getElementById('chamber-angle').innerText = Math.floor(Math.random() * 3);
            document.getElementById('chamber-rpm').innerText = Math.floor(Math.random() * 10 + 25);
            
            // Energy system
            const voltage = (Math.random() * 1.5 + 3.5).toFixed(2);
            document.getElementById('voltage').innerText = voltage;
            
            const storedEnergy = (0.5 * 10 * voltage * voltage).toFixed(1);
            document.getElementById('stored-energy').innerText = storedEnergy;
            
            const cumulativeEnergy = Math.floor(Math.random() * 100 + 300);
            document.getElementById('cumulative-energy').innerText = cumulativeEnergy;
            
            document.getElementById('avg-power').innerText = (Math.random() * 20 + 15).toFixed(1);
            
            // Energy bar
            const energyPercent = (voltage / 5) * 100;
            document.getElementById('energy-fill').style.width = energyPercent + '%';
        }

        // Update every 2 seconds
        setInterval(updateTelemetry, 2000);

        // ═════════════════════════════════════════════════════
        //                  CONTROL FUNCTIONS
        // ═════════════════════════════════════════════════════
        function startMission() {
            showNotification('✅ بدء المهمة', '#00d46a');
            console.log('Mission started');
            // Here you would send MQTT command: gravityx/commands/start
        }

        function autoTrack() {
            showNotification('🎯 تفعيل التتبع التلقائي', '#4a9eff');
            console.log('Auto-track enabled');
            // MQTT: gravityx/commands/autotrack
        }

        function emergencyStop() {
            showNotification('⚠️ إيقاف طارئ! جميع الأنظمة متوقفة', '#ff4757');
            console.log('EMERGENCY STOP!');
            // MQTT: gravityx/commands/estop
            // Play alarm sound
            playAlarm();
        }

        function alignChamber() {
            showNotification('🔄 جاري محاذاة الغرفة...', '#4a9eff');
            console.log('Aligning chamber');
        }

        function holdSync() {
            showNotification('🔒 تثبيت المزامنة', '#00d46a');
            console.log('Sync held');
        }

        function releaseBall() {
            showNotification('🚀 إطلاق الكبسولة', '#ffd700');
            console.log('Ball released');
        }

        function stopMovement() {
            showNotification('🛑 إيقاف الحركة', '#ffa502');
            console.log('Movement stopped');
        }

        function reroute() {
            showNotification('🔀 إعادة توجيه المسار', '#4a9eff');
            console.log('Rerouting path');
        }

        function correctPath() {
            showNotification('✏️ تصحيح المسار', '#00d46a');
            console.log('Path corrected');
        }

        function dischargeCO2() {
            showNotification('💨 تفريغ CO₂! إخلاء المنطقة', '#ff4757');
            console.log('CO2 discharged');
            playAlarm();
        }

        // ═════════════════════════════════════════════════════
        //                  NOTIFICATION SYSTEM
        // ═════════════════════════════════════════════════════
        function showNotification(message, color) {
            const notification = document.createElement('div');
            notification.style.position = 'fixed';
            notification.style.top = '100px';
            notification.style.right = '30px';
            notification.style.padding = '20px 30px';
            notification.style.background = color;
            notification.style.color = 'white';
            notification.style.borderRadius = '10px';
            notification.style.boxShadow = '0 10px 40px rgba(0,0,0,0.5)';
            notification.style.fontSize = '18px';
            notification.style.fontWeight = '700';
            notification.style.zIndex = '10000';
            notification.style.animation = 'slideIn 0.5s';
            notification.innerText = message;
            
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.style.animation = 'slideOut 0.5s';
                setTimeout(() => notification.remove(), 500);
            }, 3000);
        }

        // Add CSS animations
        const style = document.createElement('style');
        style.innerHTML = `
            @keyframes slideIn {
                from { transform: translateX(400px); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            @keyframes slideOut {
                from { transform: translateX(0); opacity: 1; }
                to { transform: translateX(400px); opacity: 0; }
            }
        `;
        document.head.appendChild(style);

        // ═════════════════════════════════════════════════════
        //                   ALARM SOUND
        // ═════════════════════════════════════════════════════
        function playAlarm() {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            oscillator.frequency.value = 800;
            oscillator.type = 'square';
            
            gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
            
            oscillator.start();
            
            setTimeout(() => {
                oscillator.frequency.value = 400;
            }, 200);
            
            setTimeout(() => {
                oscillator.stop();
            }, 400);
        }

        // ═════════════════════════════════════════════════════
        //                 MQTT INTEGRATION
        // ═════════════════════════════════════════════════════
        // To enable real MQTT connection, include Paho MQTT library:
        // <script src="https://unpkg.com/mqtt/dist/mqtt.min.js"></script>
        
        /*
        const client = mqtt.connect('ws://localhost:9001');
        
        client.on('connect', function() {
            console.log('Connected to Gravity X MQTT');
            client.subscribe('gravityx/telemetry/#');
            client.subscribe('gravityx/alerts/#');
        });
        
        client.on('message', function(topic, message) {
            const data = JSON.parse(message.toString());
            
            if(topic === 'gravityx/telemetry/rpm_a') {
                document.getElementById('rpm-a').innerText = data.value;
            }
            // Add more handlers...
        });
        */

        console.log('🛸 Gravity X Dashboard loaded successfully!');
        console.log('📡 Ready for MQTT integration');
    </script>

</body>
</html>
