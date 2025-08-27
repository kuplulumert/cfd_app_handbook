# Professional Premium CFD Theme

**Theme Name:** "Sigma Professional" - A premium, minimalist design system for technical CFD documentation

## Theme Overview

The Sigma Professional theme is a sophisticated, clean design system specifically crafted for technical engineering documentation, particularly CFD (Computational Fluid Dynamics) applications. It combines professional enterprise aesthetics with excellent readability and modern UI principles.

## Core Design Philosophy

- **Professional Credibility**: Builds trust through clean, enterprise-grade design
- **Enhanced Readability**: Optimized typography and spacing for technical content
- **Sophisticated Minimalism**: Clean design without unnecessary visual noise
- **Industry Standard**: Follows best practices for technical documentation

## Visual Characteristics

### Color Palette

#### Primary Colors
- **Background**: `#fafbfc` (Light gray container background)
- **Card Background**: `#ffffff` (Pure white for content cards)
- **Primary Text**: `#374151` (Dark gray for body text)
- **Emphasis Text**: `#111827` (Near black for emphasized content)

#### Accent Colors (Section-specific)
- **Overview**: `#3b82f6` (Professional Blue) with pale background `#f8faff`
- **Strengths**: `#10b981` (Success Green) with pale background `#f0fdf4`
- **Limitations**: `#f59e0b` (Warning Amber) with pale background `#fffbeb`
- **Use Cases**: `#8b5cf6` (Premium Purple) with pale background `#faf5ff`
- **Avoid**: `#ef4444` (Alert Red) with pale background `#fef2f2`
- **Tips/Guidelines**: `#06b6d4` (Info Cyan) with pale background `#f0fdfa`
- **Performance**: `#10b981` (Success Green) with pale background `#f0fdf4`
- **Pitfalls**: `#f59e0b` (Warning Amber) with pale background `#fffbeb`
- **Choice**: `#3b82f6` (Professional Blue)

#### Utility Colors
- **Borders**: `#e1e8ed` (Subtle gray borders)
- **Success Background**: `#f8fafc` (Light blue-gray)
- **Warning Background**: `#fef2f2` (Light red)

### Typography

#### Font Stack
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
```

#### Font Sizes
- **Section Headers (h3)**: `1.375rem` (22px)
- **Sub-headers (h4)**: `1.125rem` (18px)
- **Body Text**: `0.9375rem` (15px)
- **Line Height**: `1.6` for optimal readability

#### Font Weights
- **Section Headers**: `600` (Semi-bold)
- **Sub-headers**: `600` (Semi-bold)
- **Body Text**: `400` (Regular)
- **Emphasized Content**: `600` (Semi-bold via `<strong>` tags)

### Layout Structure

#### Container System
```css
.industry-guide {
    width: 100%;
    background: #fafbfc;
    padding: 3rem;
    border-radius: 12px;
    border: 1px solid #e1e8ed;
}
```

#### Card System
```css
.guide-section {
    margin-bottom: 3.5rem;
    background: #ffffff;
    border: 1px solid #e1e8ed;
    border-radius: 12px;
    padding: 2.5rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    transition: all 0.2s ease;
}

.guide-section:hover {
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    transform: translateY(-1px);
}
```

### Interactive Elements

#### Numbered Bullets
- **Design**: Rounded squares with section accent colors
- **Size**: `1.5rem × 1.5rem`
- **Auto-numbering**: CSS counters for systematic organization
- **Font**: `0.75rem` with `600` weight

#### Use Case Items
```css
.use-case-item {
    background: #f8fafc;
    border-left: 3px solid var(--accent-color);
    border-radius: 0 6px 6px 0;
    padding: 0.75rem;
}
```

#### Avoid Items
```css
.avoid-item {
    background: #fef2f2;
    border-left: 3px solid var(--accent-color);
    border-radius: 0 6px 6px 0;
    padding: 0.75rem;
}
```

### Content Highlighting System

#### Bold Key Phrases
Technical terms, values, and important concepts are highlighted using `<strong>` tags:

- **Technical Parameters**: `y⁺ > 30`, `Re > 10,000`, `±15-20% error margins`
- **Model Characteristics**: `Two-equation RANS model`, `Cannot integrate to wall`
- **Performance Metrics**: `40-50% faster than SST`, `50+ years`
- **Categories**: `Computational efficiency:`, `Mesh requirements:`

#### Emphasis Hierarchy
1. **Section Headers**: Color-coded with accent colors
2. **Sub-headers**: Bold, dark gray
3. **Key Terms**: Bold within body text
4. **Regular Text**: Medium gray for comfortable reading

## Spacing System

### Margins and Padding
- **Section Spacing**: `3.5rem` between major sections
- **Card Padding**: `2.5rem` internal padding
- **Container Padding**: `3rem` around main container
- **List Item Spacing**: `1.25rem` between bullet points
- **Header Bottom Margin**: `1.75rem` below section headers

### Responsive Breakpoints
```css
@media (max-width: 768px) {
    .container {
        padding: 0 1rem;
    }
}
```

## Component Specifications

### Navigation Integration
- **Full Width Layout**: Removes max-width constraints for modern displays
- **Header Integration**: Works with existing navigation systems
- **Tab Compatibility**: Supports tabbed content interfaces

### Accessibility Features
- **High Contrast**: Excellent text-to-background contrast ratios
- **Semantic Structure**: Proper heading hierarchy
- **Focus States**: Clear interactive element focus
- **Screen Reader Friendly**: Proper ARIA structure

## Implementation Guidelines

### CSS Architecture
1. **Container**: Main background wrapper with subtle styling
2. **Sections**: Individual content cards with hover effects
3. **Typography**: System font stack with optimized sizing
4. **Colors**: CSS custom properties for accent colors
5. **Spacing**: Consistent rem-based spacing system

### Content Structure
1. **Headers**: Numbered sections with color-coded accents
2. **Lists**: Auto-numbered bullets with content highlighting
3. **Emphasis**: Strategic use of bold for key technical terms
4. **Special Items**: Distinct styling for use cases and warnings

### Technical Requirements
- **Modern Browser Support**: CSS Grid, Flexbox, Custom Properties
- **Font Loading**: System fonts for instant rendering
- **Performance**: Minimal CSS footprint
- **Scalability**: rem-based sizing for accessibility

## Content Information Architecture

### Dual-Tab System Structure

The Sigma Professional theme employs a comprehensive dual-tab system for technical model documentation:

#### **Industry Guide Tab** (9-Section Structure)
Practical implementation and usage guidelines for engineering teams.

#### **Academy Guide Tab** (7-Section Structure)  
Theoretical foundation and mathematical derivation for researchers and advanced users.

### Industry Guide Sections (1-9)

The systematic 9-section information architecture for practical implementation (with numbered headers):

#### 1. **Model Overview** (Blue `#3b82f6`)
- Model type and classification
- Historical development and creators
- Primary characteristics and validation status
- Target Reynolds number ranges

**Content Pattern:**
- **Technical Classification**: "Two-equation RANS model"
- **Historical Context**: "First complete turbulence closure"
- **Industry Status**: "Most widely validated"
- **Application Scope**: "High Reynolds number flows"

#### 2. **Key Advantages** (Green `#10b981`)
- Computational efficiency metrics
- Convergence characteristics
- Software availability
- Validation history
- Mesh requirements flexibility

**Content Pattern:**
- **Performance Metrics**: "40-50% faster than SST"
- **Reliability Factors**: "Wide range of flow conditions"
- **Industry Adoption**: "Every commercial CFD solver"
- **Proven Track Record**: "50+ years of validation"

#### 3. **Computational Requirements** (Amber `#f59e0b`)
- Mesh specifications and limitations
- Wall treatment requirements
- Reynolds number constraints
- Known accuracy issues

**Content Pattern:**
- **Mesh Constraints**: "y⁺ > 30 for wall functions"
- **Physical Limitations**: "Cannot integrate to wall"
- **Validity Ranges**: "Re > 10,000 for validity"
- **Prediction Issues**: "Over-predicts/under-predicts"

#### 4. **Application Use Cases** (Purple `#8b5cf6`)
- Specific appliance applications
- Industry implementations
- Geometric considerations
- Scale of applications

**Content Pattern:**
- **Appliance Types**: "Refrigerators & Freezers", "Ovens & Cooktops"
- **System Scale**: "Large-Scale Systems", "Early Design Studies"
- **Application Context**: Internal air circulation, heat exchangers

#### 5. **Selection Criteria** (Blue `#3b82f6`)
- When to choose over alternatives
- Project requirements matching
- Resource considerations
- Accuracy expectations

**Content Pattern:**
- **Project Constraints**: "Time-critical projects", "Fast turnaround"
- **Flow Characteristics**: "High Reynolds flows", "Re > 50,000"
- **Geometry Types**: "Simple geometries"
- **Accuracy Requirements**: "±15-20% error margins"

#### 6. **Limitations & Avoid Cases** (Red `#ef4444`)
- Unsuitable applications
- Physical phenomena limitations
- Flow type restrictions
- Accuracy concerns

**Content Pattern:**
- **Flow Restrictions**: "Low Reynolds number flows", "Re < 10,000"
- **Physical Limitations**: "Wall-bounded flows requiring accuracy"
- **Complex Phenomena**: "Separation-dominated flows", "Swirling flows"

#### 7. **Setup Guidelines** (Cyan `#06b6d4`)
- Mesh requirements with specific values
- Solver settings and parameters
- Boundary condition specifications
- Convergence criteria

**Content Pattern:**
- **Mesh Requirements**: "y⁺ > 30", "30-300 optimal range", "< 1.3 growth ratio"
- **Solver Settings**: "< 10⁻⁴ convergence", "0.8 under-relaxation"
- **Boundary Conditions**: "1-10% turbulence intensity", "0.07 × hydraulic diameter"

#### 8. **Performance Expectations** (Green `#10b981`)
- Accuracy levels for different phenomena
- Computational performance metrics
- Comparison with other models
- Resource requirements

**Content Pattern:**
- **Accuracy Ranges**: "±10-15% for simple flows", "±20-30% for complex"
- **Performance Gains**: "60-70% fewer mesh cells", "30-40% lower memory"
- **Convergence Rates**: "50-70% fewer iterations"

#### 9. **Common Pitfalls** (Amber `#f59e0b`)
- Mesh-related issues and solutions
- Physical modeling problems
- Boundary condition mistakes
- Troubleshooting guidance

**Content Pattern:**
- **Problem-Solution Format**: "Problem: y⁺ < 30 causing breakdown. Solution: Coarsen mesh"
- **Categorized Issues**: Mesh-Related, Physical Modeling, Boundary Conditions
- **Preventive Guidance**: Best practices to avoid common mistakes

### Content Highlighting Strategy

#### Technical Parameters (Always Bold)
- **Numerical Values**: `y⁺ > 30`, `Re > 10,000`, `±15-20%`
- **Model Names**: `k-ε Standard`, `k-ω SST`
- **Performance Metrics**: `40-50% faster`, `50+ years`
- **Physical Constraints**: `Cannot integrate to wall`

#### Category Headers (Bold + Colon)
- **Specification Types**: `Mesh requirements:`, `Wall conditions:`
- **Performance Areas**: `Computational efficiency:`, `vs SST:`
- **Problem Categories**: `Mesh-Related Issues:`, `Physical Modeling:`

#### Quantitative Ranges (Bold)
- **Acceptable Ranges**: `30-300`, `1-10%`, `< 1.3`
- **Threshold Values**: `> 30`, `< 10⁻⁴`, `> 50,000`
- **Error Margins**: `±10-15%`, `±20-30%`

### Information Density Guidelines

#### Section Length Standards
- **Overview**: 4 concise bullet points
- **Advantages**: 5 key benefits with metrics
- **Requirements**: 4 major constraints
- **Applications**: 6-8 specific use cases
- **Selection**: 5 decision criteria
- **Limitations**: 6 avoid scenarios
- **Setup**: 3 subsections (Mesh, Solver, Boundary)
- **Performance**: 2 subsections (Accuracy, Computational)
- **Pitfalls**: 3 categories with solutions

#### Content Granularity
- **High-level**: Section overview and classification
- **Mid-level**: Specific parameters and ranges
- **Detailed**: Implementation guidance and troubleshooting

### Academy Guide Sections (7 Sections)

The systematic 7-section theoretical and mathematical structure for advanced users (headers WITHOUT numbers, using academic bullet points where appropriate for clear organization):

#### **Historical Context and Development**
- Timeline of model evolution and key contributors
- Theoretical breakthroughs and publications
- Evolution from earlier models
- Modern variants and improvements

**Content Pattern:**
- **Timeline Format**: "1925: Prandtl introduces mixing length", "1974: Launder & Spalding"
- **Key Contributors**: Names, institutions, and contributions
- **Theoretical Milestones**: Major developments in turbulence modeling
- **Modern Evolution**: Recent improvements and variants

#### **Mathematical Foundation and Complete Derivation**
- Reynolds-Averaged Navier-Stokes equations
- Exact transport equations and modeling assumptions
- Dimensional analysis and closure requirements
- Boussinesq eddy viscosity hypothesis

**Content Pattern:**
- **Exact Equations**: Complete mathematical formulations with KaTeX rendering
- **Modeling Steps**: Systematic derivation process
- **Dimensional Analysis**: Physical reasoning for model structure
- **Closure Approximations**: Assumptions and their justifications

#### **Comprehensive Term Definitions and Physical Meaning**
- Detailed explanation of all variables and parameters
- Physical interpretation of mathematical terms
- Scale relationships and turbulent quantities
- Units and dimensional considerations

**Content Pattern:**
- **Variable Definitions**: k, ε, ω, μt with mathematical expressions
- **Physical Meaning**: Real-world interpretation of mathematical terms
- **Scale Relationships**: Connection between different turbulent scales
- **Practical Significance**: How variables affect flow behavior

#### **Turbulent Scales and Energy Cascade Theory**
- Kolmogorov microscales and universal behavior
- Integral scales and energy-containing eddies
- Taylor microscale and inertial subrange
- Reynolds number requirements and scale separation

**Content Pattern:**
- **Scale Definitions**: Mathematical expressions for length, time, velocity scales
- **Energy Cascade**: Physical process and mathematical representation
- **Universal Laws**: -5/3 energy spectrum, Kolmogorov constants
- **Practical Implications**: Mesh requirements and model validity

#### **Model Constants: Derivation and Physical Significance**
- Detailed derivation of all model constants
- Physical reasoning and experimental calibration
- Relationships between constants
- Historical validation database

**Content Pattern:**
- **Constant Values**: Cμ = 0.09, C1ε = 1.44, etc.
- **Derivation Process**: Mathematical steps to determine values
- **Physical Basis**: Experimental observations and theoretical constraints
- **Validation Cases**: Specific flows used for calibration

#### **Advanced Theoretical Framework and Fundamental Assumptions**
- Reynolds decomposition and statistical framework
- Exact Reynolds stress transport equations
- Boussinesq approximation implications
- Anisotropy tensor analysis and model limitations

**Content Pattern:**
- **Statistical Framework**: Ensemble averaging and turbulence decomposition
- **Exact Equations**: Complete Reynolds stress transport without approximations
- **Key Assumptions**: Local equilibrium, gradient diffusion, isotropy
- **Limitation Analysis**: Where and why the model fails

#### **Advanced Model Variants and Modern Improvements**
- Low Reynolds number modifications
- Compressibility corrections
- Rotation and curvature effects
- Modern extensions and research developments

**Content Pattern:**
- **Variant Classifications**: RNG, Realizable, Low-Re modifications
- **Enhancement Mechanisms**: Mathematical modifications and their purpose
- **Application Ranges**: When to use specific variants
- **Research Frontiers**: Current developments and future directions

### Academy Guide Design Elements

#### Mathematical Presentation
- **KaTeX Integration**: Professional mathematical rendering
- **Equation Blocks**: Centered, highlighted mathematical expressions
- **Numbered Equations**: Sequential referencing system
- **Symbol Definitions**: Clear notation and units

#### Content Organization
- **Term Definitions**: Highlighted definition blocks with mathematical expressions
- **Historical Timeline**: Chronological development presentation with proper citations
- **Validation Database**: Structured experimental evidence with references
- **Advanced Topics**: Progressive complexity from basic to research-level

#### Academic Writing Standards
- **Professional Tone**: Clear, authoritative language suitable for technical documentation
- **Clean Structure**: Logical progression from historical context to advanced topics
- **Technical Accuracy**: Precise terminology without unnecessary complexity
- **Readable Format**: Flowing paragraphs that explain concepts clearly
- **Balanced Coverage**: Both theoretical foundations and practical implications

#### Enhanced Visual Design
- **Academic Aesthetics**: Clean design with subtle shadows and professional typography
- **Refined Bullets**: Circular numbered bullets with gentle shadows and hover effects
- **Professional Typography**: Clean system fonts with subtle accent indicators
- **Subtle Cards**: Minimal shadows, rounded corners, and smooth transitions
- **Pale Color Palette**: Extremely subtle background tints for section organization

#### Visual Styling for Academy Guide
```css
        .academy-guide {
            width: 100%;
            background: #ffffff;
            padding: 2rem 0;
        }

        /* Academy Guide - Academic bullet formatting */
        .academy-guide .guide-bullet {
            background: #374151;
            color: white;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            margin-top: 8px;
        }

        .academy-guide .guide-bullet::before {
            content: "";
        }

        .equation-block {
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 6px;
            padding: 1rem;
            margin: 1rem 0;
            text-align: center;
            font-size: 1rem;
            overflow-x: auto;
        }

        .term-item {
            background: #f8f9fa;
            border-left: 3px solid var(--accent-color);
            padding: 1rem;
            margin: 0.75rem 0;
            border-radius: 0 6px 6px 0;
        }

        .term-item strong {
            color: var(--accent-color);
            font-size: 1.05rem;
        }
        ```

### Content Depth Guidelines

#### Academy vs Industry Guide Differences
- **Industry Guide**: Practical values, setup procedures, troubleshooting
- **Academy Guide**: Mathematical derivations, theoretical background, research insights

#### Mathematical Rigor Levels
- **Basic Level**: Fundamental equations and simple derivations
- **Intermediate Level**: Complete mathematical development
- **Advanced Level**: Research-grade theoretical analysis

#### Content Balance
- **Mathematical Content**: 60% equations, derivations, theory
- **Practical Context**: 40% physical interpretation, applications
- **Historical Perspective**: 10% development timeline, contributors

## Usage Examples

### Dual-Tab System Implementation
```html
<!-- Content Tabs -->
<div class="content-tabs">
    <button class="content-tab active" onclick="showTab('industry')">Industry Guide</button>
    <button class="content-tab" onclick="showTab('academy')">Academy Guide</button>
</div>

<!-- Industry Guide Tab Content -->
<div id="industry" class="tab-content active">
    <div class="industry-guide">
        <!-- Industry Guide Sections -->
    </div>
</div>

<!-- Academy Guide Tab Content -->
<div id="academy" class="tab-content">
    <div class="academy-guide">
        <!-- Academy Guide Sections -->
    </div>
</div>
```

### Industry Guide Section Implementation
```html
<div class="guide-section guide-overview">
    <h3>1. Model Overview</h3>
    <ul class="guide-list">
        <li class="guide-item">
            <span class="guide-bullet">•</span>
            <span class="guide-text"><strong>Two-equation RANS model</strong> solving for turbulent kinetic energy (k) and dissipation rate (ε).</span>
        </li>
    </ul>
</div>
```

### Academy Guide Section Implementation
```html
<div class="guide-section guide-overview">
    <h3>Mathematical Foundation and Complete Derivation</h3>
    <p class="guide-text">The k-ε model emerges from the exact Reynolds stress transport equations through systematic modeling approximations.</p>
    
    <h4>Reynolds-Averaged Navier-Stokes Equations:</h4>
    <div class="equation-block">
        $$\frac{\partial \rho}{\partial t} + \frac{\partial(\rho \overline{u_i})}{\partial x_i} = 0$$
    </div>
    
    <h4>Historical Development</h4>
    <p class="guide-text">The theoretical foundations emerged through decades of systematic development, beginning with Prandtl's mixing length concept in 1925, which established the eddy viscosity hypothesis. This was followed by Kolmogorov's dimensional analysis in 1942, providing the theoretical basis for the k-ε structure. The complete model formulation was achieved by Launder and Spalding in 1974, who established the standard constants through extensive calibration against experimental data.</p>
    
    <div class="term-definitions">
        <div class="term-item">
            <strong>k:</strong> Turbulent kinetic energy per unit mass [m²/s²]
            $$k = \frac{1}{2}\overline{u_i'u_i'}$$
            <p class="guide-text"><em>Physical meaning:</em> Represents the average kinetic energy contained in turbulent fluctuations.</p>
        </div>
    </div>
</div>
```

### Content Highlighting Standards
```html
<!-- Industry Guide Highlighting -->
<span class="guide-text"><strong>Mesh requirements:</strong> <strong>y⁺ > 30</strong> for wall functions, coarser near-wall mesh acceptable.</span>

<!-- Academy Guide Mathematical Terms -->
<div class="term-item">
    <strong>μₜ:</strong> Turbulent (eddy) viscosity [kg/m·s]
    $$\mu_t = \rho C_\mu \frac{k^2}{\epsilon}$$
    <p class="guide-text"><em>Physical meaning:</em> Enhanced momentum transport due to turbulent mixing.</p>
</div>
```

### Complete Industry Guide Section Example
```html
<!-- Setup Guidelines Section -->
<div class="guide-section guide-tips">
    <h3>7. Setup and Mesh Guidelines</h3>
    
    <h4>Mesh Requirements:</h4>
    <ul class="guide-list">
        <li class="guide-item">
            <span class="guide-bullet">•</span>
            <span class="guide-text"><strong>y⁺ > 30:</strong> Essential for wall function validity (optimal range: <strong>30-300</strong>).</span>
        </li>
        <li class="guide-item">
            <span class="guide-bullet">•</span>
            <span class="guide-text"><strong>Growth ratio:</strong> <strong>< 1.3</strong> acceptable, more forgiving than SST model.</span>
        </li>
    </ul>
    
    <h4>Solver Settings:</h4>
    <ul class="guide-list">
        <li class="guide-item">
            <span class="guide-bullet">•</span>
            <span class="guide-text"><strong>Convergence:</strong> Residuals <strong>< 10⁻⁴</strong> typically sufficient for engineering accuracy.</span>
        </li>
    </ul>
</div>
```

### Complete Academy Guide Section Example
```html
<!-- Historical Context Section -->
<div class="guide-section" style="background: #f0f4f8; border-left: 4px solid #3b82f6;">
    <h3>Historical Context and Development</h3>
    <p class="guide-text">The k-ε model represents a milestone in turbulence modeling, being the first complete closure for the Reynolds-Averaged Navier-Stokes equations.</p>
    
    <h4>Timeline and Evolution:</h4>
    <ul class="guide-list">
        <li class="guide-item">
            <span class="guide-bullet">•</span>
            <span class="guide-text"><strong>1925:</strong> Prandtl introduces mixing length concept</span>
        </li>
        <li class="guide-item">
            <span class="guide-bullet">•</span>
            <span class="guide-text"><strong>1974:</strong> Launder & Spalding finalize standard k-ε model constants</span>
        </li>
    </ul>
</div>
```

### Mathematical Expression Templates
```html
<!-- Equation Block -->
<div class="equation-block">
    $$\frac{\partial(\rho k)}{\partial t} + \frac{\partial(\rho k u_i)}{\partial x_i} = G_k - \rho\epsilon + \frac{\partial}{\partial x_j}\left[\left(\mu + \frac{\mu_t}{\sigma_k}\right) \frac{\partial k}{\partial x_j}\right]$$
</div>

<!-- Term Definition -->
<div class="term-item">
    <strong>Gₖ:</strong> Shear production of turbulent kinetic energy [kg/m³·s³]
    $$G_k = \mu_t S^2 = \mu_t \left(2\overline{S_{ij}S_{ij}}\right)$$
    <p class="guide-text"><em>Physical meaning:</em> Energy transfer from mean flow to turbulent fluctuations through Reynolds stress work.</p>
</div>

<!-- Constants Table -->
<div class="constants-table">
    <div class="equation-block">
        $$C_\mu = 0.09, \quad C_{1\epsilon} = 1.44, \quad C_{2\epsilon} = 1.92$$
        $$\sigma_k = 1.0, \quad \sigma_\epsilon = 1.3$$
    </div>
</div>
```

## Theme Benefits

### For Technical Documentation
✅ **Professional Credibility**: Enterprise-grade design builds user trust  
✅ **Enhanced Readability**: Optimized for scanning technical information  
✅ **Clear Hierarchy**: Easy identification of important parameters  
✅ **Modern Aesthetics**: Contemporary design without being trendy  
✅ **Information Architecture**: Systematic organization of complex content  
✅ **Dual-Purpose Design**: Serves both practical and theoretical needs

### For Engineering Teams (Industry Guide)
✅ **Quick Reference**: Bold technical values stand out  
✅ **Systematic Navigation**: Numbered sections and clear structure  
✅ **Professional Presentation**: Suitable for client presentations  
✅ **Reduced Cognitive Load**: Clean design reduces mental fatigue  
✅ **Cross-Platform Consistency**: Works across all devices and browsers  
✅ **Implementation Focus**: Practical guidelines for immediate use

### For Researchers and Academia (Academy Guide)
✅ **Mathematical Precision**: Professional equation rendering with KaTeX  
✅ **Theoretical Depth**: Complete derivations and physical foundations  
✅ **Historical Context**: Timeline of model development and evolution  
✅ **Research Quality**: Publication-ready mathematical presentation  
✅ **Educational Value**: Progressive complexity from basic to advanced  
✅ **Reference Standards**: Comprehensive variable definitions and units

### For Multi-Audience Documentation
✅ **Content Separation**: Clear distinction between practical and theoretical  
✅ **Progressive Disclosure**: Users can choose their level of detail  
✅ **Unified Design**: Consistent visual language across both tabs  
✅ **Flexible Navigation**: Easy switching between implementation and theory  
✅ **Comprehensive Coverage**: From basic usage to research-level analysis  

## Customization Options

### Color Variations
- Accent colors can be modified per section type
- Corporate color schemes can be integrated
- Dark mode adaptation possible

### Typography Adjustments
- Font sizes can be scaled proportionally
- Font stack can include custom enterprise fonts
- Line height adjustments for different content densities

### Layout Modifications
- Card padding can be adjusted for content density
- Spacing system can be tightened or loosened
- Container widths can be constrained for specific layouts

## Maintenance Guidelines

### Consistency Rules
1. Always use the established color palette
2. Maintain spacing ratios when scaling
3. Use bold sparingly but strategically
4. Keep hover effects subtle and professional
5. Ensure accessibility standards are met

### Update Procedures
1. Test changes across different browsers
2. Verify readability on various screen sizes
3. Maintain semantic HTML structure
4. Update documentation when changes are made
5. Test with screen readers for accessibility

---

**Theme Name**: Sigma Professional  
**Version**: 1.0  
**Created**: December 2024  
**Optimized For**: Technical CFD Documentation  
**Compatible With**: Modern browsers, responsive design  
**License**: Internal use for CFD applications