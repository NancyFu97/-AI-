import random
import string
from typing import List, Dict, Tuple, Optional

class ExerciseGenerator:
    """习题自动生成AI模型"""
    
    def __init__(self):
        # 初始化题库和知识单元
        self.knowledge_units = {
            "数学": {
                "基础": ["加减乘除", "分数运算", "简单方程"],
                "中级": ["代数", "几何", "概率统计"],
                "高级": ["微积分", "线性代数", "微分方程"]
            },
            "英语": {
                "基础": ["词汇", "简单语法", "日常对话"],
                "中级": ["复杂语法", "阅读理解", "写作"],
                "高级": ["学术英语", "文学分析", "专业术语"]
            },
            "编程": {
                "基础": ["变量", "条件语句", "循环"],
                "中级": ["函数", "数据结构", "面向对象"],
                "高级": ["算法设计", "系统架构", "性能优化"]
            }
        }
        
        # 题型模板
        self.question_templates = {
            "选择题": {
                "结构": "{问题} A. {选项1} B. {选项2} C. {选项3} D. {选项4}",
                "答案格式": "正确答案: {正确选项}"
            },
            "填空题": {
                "结构": "{问题} ______",
                "答案格式": "答案: {答案}"
            },
            "简答题": {
                "结构": "{问题}",
                "答案格式": "参考答案: {答案}"
            },
            "计算题": {
                "结构": "{问题}",
                "答案格式": "解答: {答案}"
            }
        }
    
    def generate_exercise(self, 
                         subject: str, 
                         difficulty: str, 
                         question_type: str,
                         count: int = 1) -> List[Dict]:
        """
        生成指定数量的习题
        
        参数:
            subject: 科目
            difficulty: 难度级别
            question_type: 题型
            count: 生成数量
            
        返回:
            包含习题和答案的字典列表
        """
        if subject not in self.knowledge_units:
            raise ValueError(f"不支持的科目: {subject}")
        
        if difficulty not in self.knowledge_units[subject]:
            raise ValueError(f"不支持的难度级别: {difficulty}")
        
        if question_type not in self.question_templates:
            raise ValueError(f"不支持的题型: {question_type}")
        
        exercises = []
        for _ in range(count):
            # 根据科目、难度和题型生成习题
            if subject == "数学":
                question, answer = self._generate_math_question(difficulty, question_type)
            elif subject == "英语":
                question, answer = self._generate_english_question(difficulty, question_type)
            elif subject == "编程":
                question, answer = self._generate_programming_question(difficulty, question_type)
            else:
                raise ValueError(f"不支持的科目: {subject}")
            
            # 格式化习题
            formatted_question = self.question_templates[question_type]["结构"].format(**question)
            formatted_answer = self.question_templates[question_type]["答案格式"].format(** answer)
            
            exercises.append({
                "subject": subject,
                "difficulty": difficulty,
                "type": question_type,
                "question": formatted_question,
                "answer": formatted_answer
            })
        
        return exercises
    
    def _generate_math_question(self, difficulty: str, question_type: str) -> Tuple[Dict, Dict]:
        """生成数学题"""
        if difficulty == "基础":
            if question_type == "选择题":
                a, b = random.randint(1, 20), random.randint(1, 20)
                op = random.choice(["+", "-", "*"])
                
                if op == "+":
                    correct = a + b
                elif op == "-":
                    correct = a - b
                    # 确保结果为正数
                    while correct < 0:
                        a, b = random.randint(1, 20), random.randint(1, 20)
                        correct = a - b
                else:  # *
                    correct = a * b
                
                # 生成干扰选项
                options = [correct]
                while len(options) < 4:
                    wrong = correct + random.randint(-5, 5)
                    if wrong != correct and wrong not in options:
                        options.append(wrong)
                
                random.shuffle(options)
                correct_idx = options.index(correct)
                correct_option = chr(65 + correct_idx)  # A, B, C, D
                
                question = {
                    "问题": f"{a} {op} {b} 的结果是多少?",
                    "选项1": options[0],
                    "选项2": options[1],
                    "选项3": options[2],
                    "选项4": options[3]
                }
                
                answer = {"正确选项": correct_option}
                
                return question, answer
                
            elif question_type == "填空题":
                a, b = random.randint(1, 10), random.randint(1, 10)
                question = {"问题": f"{a} 乘以 {b} 等于"}
                answer = {"答案": a * b}
                return question, answer
                
        elif difficulty == "中级":
            if question_type == "计算题":
                a, b, c = random.randint(1, 5), random.randint(1, 10), random.randint(1, 10)
                question = {"问题": f"求解方程: {a}x + {b} = {c}"}
                x = (c - b) / a
                answer = {"答案": f"x = {x}"}
                return question, answer
        
        # 默认返回一个基础题
        return self._generate_math_question("基础", "选择题")
    
    def _generate_english_question(self, difficulty: str, question_type: str) -> Tuple[Dict, Dict]:
        """生成英语题"""
        if difficulty == "基础":
            if question_type == "选择题":
                words = [
                    ("苹果", "apple", ["apply", "apples", "april"]),
                    ("狗", "dog", ["cat", "duck", "door"]),
                    ("书", "book", ["look", "cook", "hook"])
                ]
                
                word, correct, distractors = random.choice(words)
                options = [correct] + distractors
                random.shuffle(options)
                correct_idx = options.index(correct)
                correct_option = chr(65 + correct_idx)
                
                question = {
                    "问题": f"'{word}'的英文单词是什么?",
                    "选项1": options[0],
                    "选项2": options[1],
                    "选项3": options[2],
                    "选项4": options[3]
                }
                
                answer = {"正确选项": correct_option}
                return question, answer
                
        elif difficulty == "中级":
            if question_type == "填空题":
                sentences = [
                    ("He ______ (go) to school every day.", "goes"),
                    ("She ______ (read) a book now.", "is reading"),
                    ("They ______ (eat) dinner last night.", "ate")
                ]
                
                sentence, answer_word = random.choice(sentences)
                question = {"问题": sentence}
                answer = {"答案": answer_word}
                return question, answer
        
        # 默认返回一个基础题
        return self._generate_english_question("基础", "选择题")
    
    def _generate_programming_question(self, difficulty: str, question_type: str) -> Tuple[Dict, Dict]:
        """生成编程题"""
        if difficulty == "基础":
            if question_type == "选择题":
                questions = [
                    {
                        "问题": "Python中，以下哪个是正确的变量名?",
                        "正确答案": "my_variable",
                        "干扰项": ["1var", "var-name", "if"]
                    },
                    {
                        "问题": "以下哪个是Python中的注释符号?",
                        "正确答案": "#",
                        "干扰项": ["//", "/* */", "--"]
                    }
                ]
                
                q = random.choice(questions)
                options = [q["正确答案"]] + q["干扰项"]
                random.shuffle(options)
                correct_idx = options.index(q["正确答案"])
                correct_option = chr(65 + correct_idx)
                
                question = {
                    "问题": q["问题"],
                    "选项1": options[0],
                    "选项2": options[1],
                    "选项3": options[2],
                    "选项4": options[3]
                }
                
                answer = {"正确选项": correct_option}
                return question, answer
                
        elif difficulty == "中级":
            if question_type == "简答题":
                questions = [
                    {
                        "问题": "请解释Python中的列表和元组有什么区别?",
                        "答案": "列表是可变的(mutable)，可以修改其中的元素；而元组是不可变的(immutable)，创建后不能修改其元素。列表使用方括号[]，元组使用圆括号()。"
                    },
                    {
                        "问题": "什么是Python中的面向对象编程?",
                        "答案": "面向对象编程是一种编程范式，它使用对象和类的概念来组织代码。类是对象的蓝图，定义了对象的属性和方法；对象是类的实例，具有类定义的属性和方法。"
                    }
                ]
                
                q = random.choice(questions)
                question = {"问题": q["问题"]}
                answer = {"答案": q["答案"]}
                return question, answer
        
        # 默认返回一个基础题
        return self._generate_programming_question("基础", "选择题")
    
    def generate_exam_paper(self, subject: str, difficulty_dist: Dict[str, int], 
                           type_dist: Dict[str, int]) -> Dict:
        """
        生成一份完整的试卷
        
        参数:
            subject: 科目
            difficulty_dist: 难度分布，如 {"基础": 5, "中级": 3, "高级": 2}
            type_dist: 题型分布，如 {"选择题": 5, "填空题": 3}
            
        返回:
            包含试卷信息和所有习题的字典
        """
        paper = {
            "subject": subject,
            "total_questions": sum(difficulty_dist.values()),
            "difficulty_distribution": difficulty_dist,
            "type_distribution": type_dist,
            "questions": []
        }
        
        # 按照难度和题型分布生成题目
        for difficulty, count in difficulty_dist.items():
            if count <= 0:
                continue
                
            # 平均分配到各种题型
            questions_per_type = count // len(type_dist)
            remaining = count % len(type_dist)
            
            for i, (q_type, _) in enumerate(type_dist.items()):
                q_count = questions_per_type + (1 if i < remaining else 0)
                if q_count <= 0:
                    continue
                    
                questions = self.generate_exercise(subject, difficulty, q_type, q_count)
                paper["questions"].extend(questions)
        
        return paper

# 使用示例
if __name__ == "__main__":
    generator = ExerciseGenerator()
    
    print("===== 生成单个习题 =====")
    math_question = generator.generate_exercise("数学", "基础", "选择题")[0]
    print(math_question["question"])
    print(math_question["answer"])
    print()
    
    print("===== 生成多个习题 =====")
    english_questions = generator.generate_exercise("英语", "中级", "填空题", 3)
    for i, q in enumerate(english_questions, 1):
        print(f"{i}. {q['question']}")
        print(f"   {q['answer']}")
    print()
    
    print("===== 生成完整试卷 =====")
    exam_paper = generator.generate_exam_paper(
        "编程",
        {"基础": 5, "中级": 3},
        {"选择题": 4, "简答题": 4}
    )
    
    print(f"科目: {exam_paper['subject']}")
    print(f"总题数: {exam_paper['total_questions']}")
    print("题目:")
    for i, q in enumerate(exam_paper["questions"], 1):
        print(f"{i}. [{q['difficulty']}][{q['type']}] {q['question']}")
        # 如需显示答案，取消下面一行的注释
        # print(f"   {q['answer']}")
