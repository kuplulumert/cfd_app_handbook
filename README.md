# Beko CFD AI Agent

A comprehensive CFD (Computational Fluid Dynamics) documentation platform designed for professional engineering teams, featuring turbulence model guides, implementation tutorials, and technical references.

## 🎨 Design System

This project implements the **Sigma Professional** theme - a premium, minimalist design system specifically crafted for technical CFD documentation.

### Theme Characteristics
- **Professional Enterprise Design**: Clean, trustworthy aesthetics
- **Enhanced Readability**: Optimized typography for technical content
- **Strategic Content Highlighting**: Bold key phrases and technical parameters
- **Systematic Organization**: Numbered sections with color-coded accents
- **Modern Responsive Layout**: Full-width design optimized for all devices

For complete theme specifications, see [`THEME_DOCUMENTATION.md`](./THEME_DOCUMENTATION.md)

## 📁 Project Structure

```
/
├── home.html                    # Landing page
├── turbulence-models.html       # Main turbulence models overview
├── time-dependency.html         # Time dependency guide
├── methods.html                 # CFD methods reference
├── product-guide.html           # Product implementation guide
├── models/                      # Individual model pages
│   ├── k-epsilon.html          # k-ε model (Sigma Professional theme)
│   ├── k-omega-sst.html        # k-ω SST model
│   ├── laminar.html            # Laminar flow model
│   └── [other models...]
├── THEME_DOCUMENTATION.md       # Complete theme specifications
└── README.md                   # This file
```

## 🔧 Technical Features

### Navigation System
- **Sticky Header**: Persistent navigation across all pages
- **Tab-based Interface**: Industry Guide and Academy Guide views
- **Breadcrumb Navigation**: Clear path hierarchy
- **Full-width Layout**: Optimized for modern displays

### Content Organization
- **Numbered Sections**: Systematic information architecture
- **Auto-numbered Lists**: CSS counter-based bullet systems
- **Content Highlighting**: Strategic bold formatting for key terms
- **Responsive Cards**: Clean, professional content containers

### Accessibility
- **High Contrast**: Optimized text-to-background ratios
- **Semantic HTML**: Proper heading hierarchy and structure
- **System Fonts**: Fast-loading, cross-platform typography
- **Keyboard Navigation**: Full accessibility support

## 🎯 Target Applications

### Primary Use Cases
- **Turbulence Model Selection**: Comprehensive guides for model choice
- **Implementation Guidelines**: Mesh, solver, and boundary condition setup
- **Performance Expectations**: Accuracy and computational requirements
- **Best Practices**: Industry-standard recommendations

### Engineering Teams
- **CFD Engineers**: Technical reference and implementation guides
- **R&D Teams**: Advanced model specifications and theory
- **Product Development**: Practical application guidelines
- **Quality Assurance**: Validation and verification procedures

## 🚀 Key Pages

### Turbulence Models Overview
- **Featured Models**: k-ε and k-ω SST (90% industry usage)
- **Complete Reference**: All available turbulence models
- **Model Comparison**: Performance and application matrix

### k-ε Model Guide (Sigma Professional Theme)
- **Industry Guide**: Practical implementation and usage
- **Academy Guide**: Theoretical foundation and mathematics
- **Setup Guidelines**: Mesh, solver, and boundary conditions
- **Performance Data**: Accuracy levels and computational costs

## 📋 Standard Information Architecture

The Sigma Professional theme employs a comprehensive **dual-tab system** for technical model documentation:

### Dual-Tab System Structure
- **Industry Guide Tab**: Practical implementation and usage guidelines (9 sections)
- **Academy Guide Tab**: Theoretical foundation and mathematical derivation (7 sections)

### Industry Guide Sections (1-9) - WITH NUMBERED HEADERS
1. **Model Overview** - Classification, history, validation status
2. **Key Advantages** - Performance metrics, reliability, industry adoption
3. **Computational Requirements** - Mesh constraints, limitations, validity ranges
4. **Application Use Cases** - Specific appliances, industry implementations
5. **Selection Criteria** - When to choose, project constraints, accuracy needs
6. **Limitations & Avoid Cases** - Flow restrictions, unsuitable applications
7. **Setup Guidelines** - Mesh requirements, solver settings, boundary conditions
8. **Performance Expectations** - Accuracy ranges, computational metrics
9. **Common Pitfalls** - Problem-solution format, troubleshooting guidance

### Academy Guide Sections (7 Sections) - FLOWING PARAGRAPHS WITHOUT BULLETS
- **Historical Context and Development** - Timeline, contributors, evolution
- **Mathematical Foundation** - Complete derivations, RANS equations
- **Term Definitions** - Physical meaning, variables, parameters
- **Turbulent Scales Theory** - Kolmogorov scales, energy cascade
- **Model Constants** - Derivation, physical significance, validation
- **Theoretical Framework** - Assumptions, limitations, Reynolds stress
- **Advanced Variants** - Modern improvements, research developments

**Note:** Academy Guide content uses clean academic format with flowing paragraphs and academic bullet points where appropriate for clear organization, following scholarly writing standards

### Content Highlighting Standards

#### Industry Guide
- **Technical Parameters**: `y⁺ > 30`, `Re > 10,000`, `±15-20%` (always bold)
- **Category Headers**: `Mesh requirements:`, `Computational efficiency:` (bold + colon)
- **Performance Metrics**: `40-50% faster`, `50+ years` (bold)
- **Physical Constraints**: `Cannot integrate to wall` (bold)

#### Academy Guide
- **Mathematical Expressions**: Professional KaTeX rendering
- **Variable Definitions**: Highlighted term blocks with equations
- **Historical Timeline**: Chronological development format
- **Physical Meaning**: Italicized explanatory text

## 📊 Design Philosophy

### Professional Standards
- **Enterprise Grade**: Suitable for client presentations
- **Technical Precision**: Accurate parameter specification
- **Systematic Organization**: Logical information flow
- **Visual Hierarchy**: Clear content prioritization

### User Experience
- **Quick Scanning**: Bold technical parameters stand out
- **Reduced Cognitive Load**: Clean, distraction-free interface
- **Professional Credibility**: Builds user trust and confidence
- **Cross-platform Consistency**: Uniform experience across devices

## 🛠 Implementation Notes

### CSS Architecture
- **Component-based Structure**: Modular, reusable components
- **Custom Properties**: CSS variables for color management
- **Responsive Design**: Mobile-first responsive principles
- **Performance Optimized**: Minimal CSS footprint

### Content Strategy
- **Technical Accuracy**: Validated CFD parameters and guidelines
- **Practical Focus**: Real-world implementation guidance
- **Progressive Detail**: Overview to detailed specifications
- **Industry Standards**: Following established CFD practices

## 📋 Browser Support

- **Modern Browsers**: Chrome, Firefox, Safari, Edge
- **CSS Features**: Grid, Flexbox, Custom Properties
- **Font Support**: System font stack for universal compatibility
- **Responsive**: Mobile, tablet, and desktop optimized

## 🔄 Maintenance

### Theme Consistency
- Follow Sigma Professional theme specifications
- Maintain established color palette and typography
- Use semantic HTML structure
- Test across different screen sizes

### Content Updates
- Verify technical accuracy of CFD parameters
- Update model recommendations based on industry trends
- Maintain consistent formatting and structure
- Test accessibility compliance

## 📝 License

Internal use for CFD applications and technical documentation.

---

**Project**: Beko CFD AI Agent  
**Theme**: Sigma Professional v1.0  
**Optimized For**: Technical CFD Documentation  
**Last Updated**: December 2024