export type SkillGap = {
  skill: string;
  student_level: number;
  required_level: number;
  gap: number;
  priority: "HIGH" | "MEDIUM" | "LOW";
  reason: string;
};
