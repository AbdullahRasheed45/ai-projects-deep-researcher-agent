# 🔍 Deep Researcher Agent

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF6B35?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Agno](https://img.shields.io/badge/Agno-Framework-purple?style=for-the-badge)](https://agno.dev/)
[![ScrapeGraph](https://img.shields.io/badge/ScrapeGraph-00D4AA?style=for-the-badge)](https://scrapegraphai.com/)

## Overview

**Deep Researcher Agent** is an intelligent research automation system that transforms complex research topics into comprehensive, well-sourced reports. Built with the Agno framework and powered by Nebius AI, this agent conducts multi-stage research workflows that rival human researchers in depth and thoroughness.

From initial topic scoping to final synthesis, the system autonomously searches the web, extracts relevant information, analyzes sources for quality and relevance, and produces coherent research reports with proper citations.

### Key Features

- **Multi-Stage Research Pipeline**: Automated workflow from scoping to final report generation
- **Intelligent Web Scraping**: ScrapeGraph integration for structured content extraction
- **Source Quality Analysis**: AI-powered evaluation of source credibility and relevance
- **Comprehensive Synthesis**: Coherent report generation with proper citations and evidence
- **Interactive Interface**: Streamlit-based UI with real-time progress tracking
- **Dual Execution Modes**: Interactive web interface or programmatic CLI access
- **Configurable Depth**: Adjustable research scope and analysis thoroughness

### Perfect For

- **Research Professionals**: Accelerate literature reviews and market research
- **Content Creators**: Generate well-researched articles and reports
- **Business Analysts**: Conduct competitive analysis and market intelligence
- **Academic Researchers**: Preliminary research and source discovery
- **Journalists**: Background research and fact-checking support
- **Consultants**: Client research and industry analysis

## Architecture

The system employs a sophisticated multi-stage research methodology:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Research      │ ──▶│   AI Research    │ ──▶│   Web Sources   │
│   Topic         │    │   Agent          │    │                 │
│                 │    │   (Nebius AI)    │    │ • Search Results│
│ "AI in          │    │                  │    │ • Web Pages     │
│  Healthcare"    │    │ • Topic Scoping  │    │ • Academic      │
│                 │    │ • Query Planning │    │ • News Articles │
└─────────────────┘    │ • Source Analysis│    │ • Reports       │
                       │ • Synthesis      │    └─────────────────┘
                       └──────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Research Pipeline │
                    │                     │
                    │ 1. Scope & Plan     │
                    │ 2. Search & Discover│
                    │ 3. Scrape & Extract │
                    │ 4. Analyze & Verify │
                    │ 5. Synthesize Report│
                    └─────────────────────┘
```

## Project Structure

```
.
├── agents.py          # Research orchestration and pipeline logic
├── app.py            # Streamlit web interface
├── .env.example      # Environment variable template
├── requirements.txt  # Python dependencies
├── .gitignore       # Git ignore patterns
├── LICENSE          # MIT license
└── README.md        # This documentation
```

## Quick Start

### Prerequisites

- Python 3.10 or higher
- Nebius AI API key
- ScrapeGraph AI API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AbdullahRasheed45/ai-projects-deep-researcher-agent.git
   cd ai-projects-deep-researcher-agent
   ```

2. **Set up environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys:
   # NEBIUS_API_KEY=your_nebius_api_key
   # SGAI_API_KEY=your_scrapegraph_api_key
   ```

### Launch Options

**Interactive Web Interface:**
```bash
streamlit run app.py
```
Access the research dashboard at `http://localhost:8501`

**Command Line Interface:**
```bash
python -c "from agents import run_research; print(run_research('Artificial Intelligence in Healthcare'))"
```

## Research Pipeline

### Stage 1: Topic Scoping
- **Objective**: Define research boundaries and key questions
- **Process**: Analyze the input topic and generate focused research questions
- **Output**: Structured research scope with primary and secondary objectives

```python
# Example scoping output:
scope = {
    "primary_questions": [
        "What are current applications of AI in healthcare?",
        "What are the main challenges and limitations?",
        "What does the future landscape look like?"
    ],
    "research_domains": ["medical_imaging", "drug_discovery", "clinical_decision_support"],
    "source_priorities": ["academic_papers", "industry_reports", "regulatory_documents"]
}
```

### Stage 2: Search & Discovery
- **Objective**: Identify high-quality sources across the web
- **Process**: Generate targeted search queries and collect promising results
- **Output**: Curated list of sources with relevance scores

```python
# Search strategy example:
search_queries = [
    "AI healthcare applications 2024",
    "machine learning medical diagnosis",
    "artificial intelligence clinical trials",
    "healthcare AI regulatory challenges"
]
```

### Stage 3: Content Extraction
- **Objective**: Extract structured information from identified sources
- **Process**: Use ScrapeGraph to intelligently scrape and parse content
- **Output**: Clean, structured content with metadata

```python
# Extraction configuration:
scrape_config = {
    "extract_sections": ["abstract", "introduction", "conclusions"],
    "preserve_citations": True,
    "filter_ads_navigation": True,
    "respect_robots_txt": True
}
```

### Stage 4: Source Analysis
- **Objective**: Evaluate source quality and extract key insights
- **Process**: AI-powered analysis of credibility, relevance, and evidence quality
- **Output**: Analyzed content with quality scores and key findings

```python
# Analysis criteria:
analysis_framework = {
    "credibility_factors": ["author_expertise", "publication_venue", "peer_review"],
    "relevance_scoring": "topic_alignment_percentage", 
    "evidence_quality": ["methodology", "sample_size", "statistical_significance"],
    "bias_detection": ["funding_sources", "conflicts_of_interest"]
}
```

### Stage 5: Synthesis & Report Generation
- **Objective**: Create coherent, comprehensive research report
- **Process**: Synthesize findings across sources into structured narrative
- **Output**: Professional research report with citations

## Usage Examples

### Academic Research
```python
# Research query
topic = "Impact of Large Language Models on Scientific Research"

# Generated report sections:
# 1. Executive Summary
# 2. Current Applications in Research
# 3. Methodological Advantages and Limitations  
# 4. Ethical Considerations and Bias
# 5. Future Directions and Recommendations
# 6. Conclusion
# 7. References and Sources
```

### Market Intelligence
```python
# Business research query  
topic = "Competitive Landscape of Cloud Vector Databases"

# Analysis includes:
# - Market size and growth projections
# - Key players and their differentiators
# - Technology trends and adoption patterns
# - Pricing models and business strategies
# - Customer segments and use cases
# - Regulatory and compliance considerations
```

### Industry Analysis
```python
# Policy research query
topic = "EU AI Act Implementation Timeline and Business Impact"

# Comprehensive coverage:
# - Regulatory timeline and milestones
# - Compliance requirements by AI system type
# - Industry-specific implications
# - Cost estimates and resource requirements
# - Best practices for preparation
# - Expert opinions and predictions
```

## Advanced Configuration

### Research Depth Control

```python
# Customize research thoroughness
research_config = {
    "search_results_per_query": 20,        # Number of initial results
    "max_sources_to_scrape": 15,           # Deep analysis limit
    "content_extraction_depth": "full",    # full, summary, keywords
    "analysis_detail_level": "comprehensive", # brief, standard, comprehensive
    "synthesis_style": "academic"          # academic, business, journalistic
}
```

### Source Quality Filters

```python
# Configure source selection criteria
quality_filters = {
    "min_credibility_score": 0.7,          # 0.0-1.0 scale
    "preferred_source_types": [
        "academic_papers", 
        "government_reports",
        "established_news_outlets",
        "industry_white_papers"
    ],
    "exclude_domains": ["unreliable-source.com"],
    "date_range": "last_2_years",           # Recency filter
    "language_preference": "english"
}
```

### Output Customization

```python
# Tailor report format and style
report_config = {
    "format": "markdown",                   # markdown, html, plain_text
    "citation_style": "apa",               # apa, mla, chicago
    "include_executive_summary": True,
    "include_methodology_section": False,
    "max_report_length": 5000,            # Words
    "include_source_quality_scores": True,
    "add_research_limitations": True
}
```

## Integration Capabilities

### API Integration

```python
# Programmatic usage for integration
from agents import DeepResearchAgent

agent = DeepResearchAgent(
    nebius_api_key="your_key",
    scrapegraph_api_key="your_key"
)

# Async research execution
research_result = await agent.research_async(
    topic="Climate Change Mitigation Technologies",
    depth="comprehensive",
    max_sources=20
)

# Access structured results
report = research_result.final_report
sources = research_result.source_analysis
methodology = research_result.research_methodology
```

### Batch Processing

```python
# Multiple topic research
topics = [
    "Quantum Computing Commercial Applications",
    "Sustainable Energy Storage Solutions", 
    "Edge AI Hardware Developments"
]

batch_results = agent.batch_research(
    topics=topics,
    parallel_execution=True,
    shared_source_optimization=True
)
```

### Custom Tool Integration

```python
# Extend with specialized research tools
class CustomResearchAgent(DeepResearchAgent):
    def add_domain_tools(self):
        # Add specialized scrapers
        self.add_tool("academic_scraper", PubMedScraper())
        self.add_tool("patent_analyzer", PatentDatabaseTool())
        self.add_tool("financial_data", BloombergAPI())
        
    def custom_analysis_pipeline(self, content):
        # Domain-specific analysis logic
        return enhanced_analysis
```

## Quality Assurance

### Source Verification

- **Credibility Scoring**: Multi-factor assessment of source reliability
- **Cross-Referencing**: Verification of claims across multiple sources
- **Bias Detection**: Identification of potential conflicts of interest
- **Fact-Checking**: Comparison with authoritative reference sources

### Report Quality Metrics

```python
quality_metrics = {
    "source_diversity": "Geographic, temporal, and perspective diversity",
    "evidence_strength": "Quality and quantity of supporting evidence", 
    "logical_coherence": "Consistency and flow of arguments",
    "citation_accuracy": "Proper attribution and link verification",
    "comprehensiveness": "Coverage of key aspects and viewpoints"
}
```

## Troubleshooting

### Common Issues

**"Empty or short reports"**
- Increase search depth and source limits
- Broaden topic scope or add related keywords
- Check domain filters and source exclusions
- Verify API rate limits and quotas

**"Scraping failures"**
- Sites may block automated access
- Reduce concurrent scraping requests
- Add retry logic and fallback strategies
- Check robots.txt compliance

**"Poor source quality"**
- Adjust credibility score thresholds
- Review source type preferences
- Add domain-specific quality filters
- Implement manual source curation

**"API authentication errors"**
- Verify API keys in environment variables
- Check API key permissions and usage limits
- Ensure proper environment loading
- Test API connectivity separately

### Performance Optimization

**Speed Improvements:**
- Enable parallel source processing
- Implement intelligent caching
- Use faster AI models for preliminary analysis
- Optimize scraping concurrency

**Quality Enhancement:**
- Increase source diversity requirements
- Add specialized domain scrapers
- Implement iterative research refinement
- Use larger context AI models

## Contributing

We welcome contributions to enhance research capabilities!

### Development Guidelines

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/research-enhancement`
3. Follow responsible web scraping practices
4. Test with diverse research topics
5. Submit pull request with example outputs

### Contribution Areas

- **Specialized Scrapers**: Domain-specific content extraction tools
- **Quality Metrics**: Enhanced source credibility assessment
- **Export Formats**: PDF, Word, and structured data outputs
- **Integration APIs**: Connections to research databases and tools
- **Multilingual Support**: Research in multiple languages
- **Advanced Analytics**: Research trend analysis and insights

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **[Agno Framework](https://agno.dev/)** for AI agent orchestration
- **[Nebius AI](https://nebius.ai/)** for powerful language model capabilities  
- **[ScrapeGraph AI](https://scrapegraphai.com/)** for intelligent web scraping
- **[Streamlit](https://streamlit.io/)** for rapid web application development
- **Research Community** for methodological best practices

## 📞 Connect & Support

<div align="center">

### 🚀 Ready to Automate Your Research Process?

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://techvibes360.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdullahrasheed-/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdullahrasheed45@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AbdullahRasheed45)

**Let's make comprehensive research accessible and automated!**

</div>

---

*Built with ❤️ by Muhammad Abdullah Rasheed. Ready to revolutionize your research workflow?*
