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
- **Overview**: `#3b82f6` (Professional Blue)
- **Strengths**: `#10b981` (Success Green)
- **Limitations**: `#f59e0b` (Warning Amber)
- **Use Cases**: `#8b5cf6` (Premium Purple)
- **Avoid**: `#ef4444` (Alert Red)
- **Tips/Guidelines**: `#06b6d4` (Info Cyan)
- **Performance**: `#10b981` (Success Green)
- **Pitfalls**: `#f59e0b` (Warning Amber)
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

### Standard Section Outline (9-Section Structure)

The Sigma Professional theme follows a systematic 9-section information architecture for technical model documentation:

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

## Usage Examples

### Section Implementation
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

### Content Highlighting
```html
<span class="guide-text"><strong>Mesh requirements:</strong> <strong>y⁺ > 30</strong> for wall functions, coarser near-wall mesh acceptable.</span>
```

### Complete Section Example
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

## Theme Benefits

### For Technical Documentation
✅ **Professional Credibility**: Enterprise-grade design builds user trust  
✅ **Enhanced Readability**: Optimized for scanning technical information  
✅ **Clear Hierarchy**: Easy identification of important parameters  
✅ **Modern Aesthetics**: Contemporary design without being trendy  
✅ **Information Architecture**: Systematic organization of complex content  

### For Engineering Teams
✅ **Quick Reference**: Bold technical values stand out  
✅ **Systematic Navigation**: Numbered sections and clear structure  
✅ **Professional Presentation**: Suitable for client presentations  
✅ **Reduced Cognitive Load**: Clean design reduces mental fatigue  
✅ **Cross-Platform Consistency**: Works across all devices and browsers  

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