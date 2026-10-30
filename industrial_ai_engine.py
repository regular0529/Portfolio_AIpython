# ==============================================================================
# 김정규 산업공학 & AI 알고리즘 패키지 (industrial_ai_engine.py)
# 소속: 부산대학교 공과대학 산업공학과
# 목적: 생산계획 최적화(LP), 센서 시계열 이상치 탐지(Z-Score), 공정 스케줄링(SPT)
# ==============================================================================

import math
import random

def solve_production_lp(cap_mach=120, cap_labor=100):
    c1, c2 = 30000, 25000
    candidates = [(0, 0, 0)]
    
    xA = cap_mach / 2.0
    if 1 * xA <= cap_labor:
        candidates.append((xA, 0, xA * c1))
        
    yB = cap_labor / 2.0
    if 1 * yB <= cap_mach:
        candidates.append((0, yB, yB * c2))
        
    det = 2 * 2 - 1 * 1
    inter_A = (2 * cap_mach - cap_labor) / det
    inter_B = (2 * cap_labor - cap_mach) / det
    if inter_A >= 0 and inter_B >= 0:
        candidates.append((inter_A, inter_B, inter_A * c1 + inter_B * c2))
        
    best_A, best_B, max_profit = max(candidates, key=lambda item: item[2])
    return {
        "best_A": best_A,
        "best_B": best_B,
        "max_profit": max_profit,
        "cap_mach": cap_mach,
        "cap_labor": cap_labor
    }

def detect_sensor_anomalies(data=None, threshold_z=2.5):
    if data is None:
        random.seed(42)
        data = [10.0 + random.gauss(0, 0.8) for _ in range(25)]
        data[14] = 16.5
        data[19] = 17.2
        
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_val = math.sqrt(variance)
    
    anomalies = []
    for i, val in enumerate(data):
        z = abs(val - mean_val) / std_val if std_val > 0 else 0
        if z > threshold_z:
            anomalies.append({"timestep": i, "value": val, "z_score": z})
            
    return {
        "mean": mean_val,
        "std": std_val,
        "threshold_z": threshold_z,
        "anomalies": anomalies,
        "total_samples": len(data)
    }

def evaluate_job_scheduling(jobs=None):
    if jobs is None:
        jobs = [
            {"id": "Job-1", "p_time": 12, "due": 20},
            {"id": "Job-2", "p_time": 4,  "due": 10},
            {"id": "Job-3", "p_time": 7,  "due": 15},
            {"id": "Job-4", "p_time": 18, "due": 25},
            {"id": "Job-5", "p_time": 2,  "due": 8},
        ]
        
    def run_rule(order):
        curr = 0
        flow = 0
        tardiness = 0
        for j in order:
            curr += j["p_time"]
            tard = max(0, curr - j["due"])
            tardiness += tard
            flow += curr
        return curr, tardiness, flow / len(order)

    makespan_fifo, tard_fifo, flow_fifo = run_rule(jobs)
    spt_order = sorted(jobs, key=lambda x: x["p_time"])
    makespan_spt, tard_spt, flow_spt = run_rule(spt_order)
    
    return {
        "fifo": {"makespan": makespan_fifo, "tardiness": tard_fifo, "avg_flow": flow_fifo},
        "spt": {"makespan": makespan_spt, "tardiness": tard_spt, "avg_flow": flow_spt}
    }

if __name__ == "__main__":
    print("=" * 60)
    print(" [부산대학교 산업공학과 김정규] 산업 AI & 최적화 엔진 실행")
    print("=" * 60)
    
    lp_res = solve_production_lp(120, 100)
    print(f"\n1. [선형계획법 최적 생산 계획]")
    print(f"   제품 A 생산: {lp_res['best_A']:.1f}개 | 제품 B 생산: {lp_res['best_B']:.1f}개")
    print(f"   예상 최대 이익: ₩{int(lp_res['max_profit']):,} 원")
    
    ano_res = detect_sensor_anomalies()
    print(f"\n2. [진동 센서 시계열 이상치 탐지]")
    print(f"   평균: {ano_res['mean']:.2f}g | 표준편차: {ano_res['std']:.2f}")
    print(f"   검출된 이상치 건수: {len(ano_res['anomalies'])}건")
    for a in ano_res['anomalies']:
        print(f"   -> 시점 {a['timestep']:02d}: {a['value']:.2f}g (Z-Score: {a['z_score']:.2f})")
        
    sch_res = evaluate_job_scheduling()
    print(f"\n3. [단일 설비 작업 스케줄링 휴리스틱 비교]")
    print(f"   FIFO 총 지연시간: {sch_res['fifo']['tardiness']}시간 (평균체류 {sch_res['fifo']['avg_flow']:.1f}시간)")
    print(f"   SPT  총 지연시간: {sch_res['spt']['tardiness']}시간 (평균체류 {sch_res['spt']['avg_flow']:.1f}시간)")
    improvement = ((sch_res['fifo']['tardiness'] - sch_res['spt']['tardiness']) / sch_res['fifo']['tardiness']) * 100
    print(f"   >>> SPT 적용 시 납기 지연 {improvement:.1f}% 개선 달성")
    print("=" * 60)
